import a2s
from socket import gaierror, timeout
from os import system


class Manager(object):
    password = None
    servers = {}

    def __init__(self, servers):
        # Set up servers
        for name in servers:
            server = servers[name]
            if "host" not in server or "port" not in server:
                raise ValueError(f"Missing host or port value for server \"{name}\"")
            self.servers[name] = Host(server["host"], server["port"])

    def safe_restart(self, threshold=0, test_run=False):
        for name in self.servers:
            try:
                players = self.servers[name].get_players()
            except (gaierror, timeout):
                print(f"Warning: Server \"{name}\" could not be reached and may be offline!")
                continue
            if len(players) > threshold:
                print(f"Server \"{name}\" will not be restarted as it has {players} players online.")
                continue
            print(f"Server \"{name}\" will be restarted...")
            command = f"docker stop {name}; docker start {name}"
            if test_run:
                print(command)
            else:
                system(command)


class Host(object):
    address = None

    def __init__(self, host, port=27015):
        self.address = (host, port)

    def get_info(self):
        return a2s.info(self.address)

    def get_rules(self):
        return a2s.rules(self.address)

    def get_players(self):
        return a2s.players(self.address)

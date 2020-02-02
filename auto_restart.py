import json
from os import chdir, path
from manager import Manager


def main():
    chdir(path.abspath(__file__))
    servers = json.load("servers.json")
    manager = Manager(servers)
    manager.safe_restart()

1
if __name__ == "__main__":
    main()
import json
from os import chdir, path
from manager import Manager


def main():
    chdir(path.dirname(path.abspath(__file__)))
    with open("servers.json", "r") as file:
        servers = json.load(file)
    manager = Manager(servers)
    manager.safe_restart()


if __name__ == "__main__":
    main()

#!/usr/bin/python3
from devices import NetworkDevice


class Router(NetworkDevice):

    def __init__(self, hostname, password="cisco", enablePassword="class", banner="Authorized Users Only!"):
        NetworkDevice.__init__(self, hostname=hostname, password=password,
                               enablePassword=enablePassword, banner=banner)
        self.modules = ['Console', 'FastEthernet0', 'GigabitEthernet0']

    def setDHCPServer(self, number, name, addr) -> None:
        pass


if __name__ == "__main__":
    pass
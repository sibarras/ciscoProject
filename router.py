#!/usr/bin/python3
import os


class Router:

    def __init__(self, hostname, enablePassword="class", password="cisco"):
        self.hostname = hostname
        self.password = password
        self.enablePass = enablePassword

    def initialConfiguration(self, banner="Authorized Users Only!"):
        vtyMax = 4  # es la cantidad de puertos para vty
        commands = f"""
            enable
            configure terminal
            
            hostname {self.hostname}
            no ip domain-lookup
            enable secret {self.enablePass}
            
            line console 0
            password {self.password}
            login logging synchronous
            exit
            
            line vty 0 {vtyMax}
            password {self.password}
            login
            exit
            
            service password-encryption
            banner motd $ {banner} $
            
        """
        self.initCommandList = commands.split("\n")
        for command in self.initCommandList:
            os.system(command)


if __name__ == '__main__':
    pass

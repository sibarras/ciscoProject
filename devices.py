import os

class NetworkDevice:

    def __init__(self, hostname=str,
                 enablePassword="class", password="cisco",
                 banner="Authorized Users Only!"):

        self.hostname = hostname
        self.password = password
        self.enablePassword = enablePassword
        self.interfaceTypes = []
        self.interfaces = []
        self.networkConnections = []

        vtyMax = 4  #vty ports number
        commands = f"""
            enable
            configure terminal
            
            hostname {self.hostname}
            no ip domain-lookup
            enable secret {self.enablePassword}
            
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
            end
        """
        for command in commands.split('\n'):
            os.system(command)
        print("The initial configuration is successfully completed!")


    def setGateway(self, gatewayIP=str) -> str:
        self.gateway = gatewayIP
        commands = f"""
            configure terminal
            ip default-gateway {gatewayIP}
            end
        """
        for command in commands.split('\n'):
            os.system(command)
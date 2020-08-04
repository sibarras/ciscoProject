import os
# Averiguar como puedes tomar

class NetworkDevice:

    def __init__(self, hostname=str,
                 enablePassword="class", password="cisco",
                 banner="Authorized Users Only!"):

        self.hostname = hostname
        self.__password = password
        self.__enablePassword = enablePassword
        self.modules = []
        self.interfaces = {}
        self.networkConnections = []

        vtyMax = 4  #vty ports number
        commands = f"""
            enable
            configure terminal
            
            hostname {self.hostname}
            no ip domain-lookup
            enable secret {self.__enablePassword}
            
            line console 0
            password {self.__password}
            login logging synchronous
            exit
            
            line vty 0 {vtyMax}
            password {self.__password}
            login
            exit
            
            service password-encryption
            banner motd $ {banner} $
            end
        """
        for command in commands.split('\n'):
            print(command)# os.system(command)  # Do in cisco Router

        self.__save()
        print(f"The initial configuration in {self.hostname} is successfully completed!")


    def __save(self):
        command = "copy running-config startup-config"
        print(command)  # os.system(command)

    def openCommunication(self):
        pass

    def closeCommunication(self):
        pass

    def connection(self, other):
        pass

    def __sub__(self, other):
        self.connection(other)

    def setGateway(self, gatewayIP=str) -> str:
        self.gateway = gatewayIP
        commands = f"""
            configure terminal
            ip default-gateway {gatewayIP}
            end
        """
        for command in commands.split('\n'):
            print(command)# os.system(command)
        
        self.__save()
        print("Gateway Sucessfully Configured!")

#!/usr/bin/python3
import os
from devices import NetworkDevice
# como lo tengo pensado, todos los resutlados de las funciones que defina deben ser
# strings para poder ser utilizadas por la terminal como inputs. Si quiero incluir alguna de estas
# funciones dentro de otra, lo que debo hacer es que esta funcion retorne un string
class Switch(NetworkDevice):

    def __init__(self, hostname, password="cisco", enablePassword="class", banner="Authorized Users Only!"):
        NetworkDevice.__init__(self, hostname=hostname, password=password,
                               enablePassword=enablePassword, banner=banner)

    def setVLAN(self, number, name, addr) -> None:
        pass


if __name__ == "__main__":
    sw1 = Switch(hostname="SW1", password="cisco", enablePassword="class", banner="Keep Out!")
    sw1.setGateway("192.168.10.10")

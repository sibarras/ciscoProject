#!/usr/bin/python3
from devices import NetworkDevice
# como lo tengo pensado, todos los resutlados de las funciones que defina deben ser
# strings para poder ser utilizadas por la terminal como inputs. Si quiero incluir alguna de estas
# funciones dentro de otra, lo que debo hacer es que esta funcion retorne un string
class Switch(NetworkDevice):

    def __init__(self, hostname=str, password=str, enablePassword=str, banner=str):
        NetworkDevice.__init__(self, hostname=hostname, password=password,
                               enablePassword=enablePassword, banner=banner)

        self.modules = [('Console', 1), ('FastEthernet0', 12), ('GigabitEthernet0', 12)]
        for module in self.modules:
            if module[1] == 1:
                self.interfaces[module[0]] = [module[0]]
            elif module[1] > 1:
                self.interfaces[module[0]] = [f'{module[0]}/{interface+1}' for interface in range(module[1])]

    def setVLAN(self, number, name, addr) -> None:
        pass


if __name__ == "__main__":
    pass

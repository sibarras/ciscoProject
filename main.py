#!/usr/bin/python3
import secretKeys as secret
from router import Router
from switch import Switch

def main():  # Programa principal
    # Routers
    RINT = Router('RINT', secret.ENABLE_PASSWORD, secret.CONSOLE_PASSWORD)
    RoExt = Router('RoExt', secret.ENABLE_PASSWORD, secret.CONSOLE_PASSWORD)
    RBor1 = Router('RBor1', secret.ENABLE_PASSWORD, secret.CONSOLE_PASSWORD)
    RBor2 = Router('RBor2', secret.ENABLE_PASSWORD, secret.CONSOLE_PASSWORD)
    
    #Switches
    SW1 = Switch('SW1', secret.ENABLE_PASSWORD, secret.CONSOLE_PASSWORD)
    SW2 = Switch('SW2', secret.ENABLE_PASSWORD, secret.CONSOLE_PASSWORD)
    SW3 = Switch('SW3', secret.ENABLE_PASSWORD, secret.CONSOLE_PASSWORD)
    SwExt = Switch('SwExt', secret.ENABLE_PASSWORD, secret.CONSOLE_PASSWORD)

    print(SW1.interfaces)

if __name__ == '__main__':
    main()

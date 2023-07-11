import os
import acudientes
def MainMenu():
    os.system("clear")
    mainMenu = True
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^16}{}{:^17}|".format(' ','ADMINISTRACION DE COMPRAS',' '))
    print('+','-'*55,'+')
    print("1. Registrar camper")
    print("2. Buscar camper")
    print("3. Eliminar camper")
    print("4. Editar camper")
    print("5. Regresar menu principal")
    opcion =int(input(":)_"))
    if (opcion == 1):
        pass
    elif (opcion == 2):
        pass
    elif (opcion == 3):
        pass
    elif (opcion == 4):
        pass
    elif (opcion == 5):
        mainMenu = False
    if mainMenu:
        MainMenu()
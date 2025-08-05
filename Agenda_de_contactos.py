import os

def mostrar_menu():
    os.system('cls')
    print('1. Mostrar los contactos')
    print('2. Crear contacto')
    print('3. Modificar contacto')
    print('0. Cerrar Menu')



def mostrar_contactos(list):
    contador = 0
    print("\nLista de Contactos.")
    for contacto in list.values():
        for clave,valor in contacto.items():
            contador +=1
            print(f'{contador}.{clave} {valor}')
    print('\n')
    
    
lista_de_contactos = {}
contador_usuarios = 0

while True:
    contacto_nuevo = {}
    mostrar_menu()
    opcion = input('Ingrese la opcion deseada:')
    
    if opcion == '1':
        mostrar_contactos(lista_de_contactos)
        
           
        
    elif opcion == '2':
        
        nombre = input('Ingrese el Nombre del contacto:')
        numero = input('Ingrese el Numero del contacto:')
        contador_usuarios += 1
        contacto_nuevo[nombre] = numero
        lista_de_contactos[f'Contacto {contador_usuarios}'] = contacto_nuevo

    elif opcion == '3':
        contacto_nuevo = {}
        print('Ingrese el usuario que desea modificar segun su indice.')
        mostrar_contactos(lista_de_contactos)
        
        opcion2 = input('Ingrese su respuesta:')
        nombre = input('Ingrese el Nombre del contacto:')
        numero = input('Ingrese el Numero del contacto:')
        contacto_nuevo[nombre] = numero
        lista_de_contactos[f'Contacto {opcion2}'] = contacto_nuevo 
        
    elif opcion == '0':
        break
    
    pausa=input('Presione enter para continuar')
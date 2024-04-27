user1 = None 
pass1 = None
user2 = None
pass2 = None
user3 = None
pass3 = None

while True:
    print("1. Iniciar Sesion")
    print("2.Registro usuario")
    print("3.Salir")
    try:
        opcion = int(input("ingrese una opcion"))
        if opcion > 0 and opcion < 4:
            if opcion == 1:
                print("1.Iniciar sesion")
                if(user1 is None and pass1 is None) and (user2 is None and pass2 is None) and (user3 is None and pass3 is None):
                   print("no existen usuarios, favor registrarse")
                   continue
                else:
                    username = input("ingrese su usuario")
                    password = input("ingrse password")
                    if (username == user1 and password == pass1):
                        while True:
                            while True:
                             print("1.Realizar llamada")
                             print("2.Enviar correo")
                             print("3.Salir")
                             try:
                                opcion2 = int(input("ingrese una opcion"))
                                if opcion2 > 0 and opcion2 < 4:
                                    if opcion2 == 1:
                                        print("realizar llamada")
                                    elif opcion2 == 2:
                                        print("enviar correo electronico")
                                    elif opcion2 == 3:
                                        print("Salir")
                                        break
                             except:
                                print("opcion ingresada no existe")
            elif opcion == 2:
                print("2.Registro usuario")
                user1 = input("ingrese usuario")
                pass1 = input("ingrese password")
                usuario = int(input("Desea agregar otro usuario? 1.si 2.no"))
                if usuario == 1:
                   user2 = input("ingrese usuario")
                   pass2 = input("ingrese password")
                   usuario = int(input("Desea agregar otro usuario? 1.si 2.no"))
                   if usuario == 1:
                    user3 = input("ingrese usuario")
                    pass3 = input("ingrese password")
                    print("usuarios creados")
                    
            elif opcion ==3:
                print("3. salir")
                break
            else:
                print("opcion no existe")
    except:
        print("opcion ingresada no existe")   
                    
                                        
                                    
                                    
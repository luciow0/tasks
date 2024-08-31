from time import sleep
import os 
import signal

class TimeoutException(Exception): 
    pass

#raise: levantaz/alzar/subir; used to throw (or raise) an exception
def timeout_handler(signum, frame):
    raise TimeoutException

def main():
    file = open("/home/luciowo/scripts_inicio/tareas.txt", 'r+')
    cant_lineas = file.readlines()
    file.close()

    #Muestra de tareas
    print("Tenes pendiente realizar las siguientes tareas","(",len(cant_lineas),"):")
    for i in range (len(cant_lineas)):
        print(i + 1,"-",cant_lineas[i]) 
    sleep(0.3)

    #Configurar señal para el timeout
    signal.signal(signal.SIGALRM, timeout_handler)
   
    #Activar/no modo interactivo
    modo_interactivo = False    
    print("Queres entrar al modo interactivo? (1, si) (0, no) " )
    while True: 
        try:
            signal.alarm(10)  # Tiempo límite de 10 segundos
            interactivo = int(input("Elige una opción: "))
            signal.alarm(0)  # Cancelar alarma si se responde a tiempo
            if interactivo == 1 or interactivo == 0: 
                break
            else: 
                print("Por favor ingresa 1 o 0 para continuar putito rico ")

        except (TimeoutException):
            print("\nTiempo agotado. Asumiendo respuesta negativa, si me odias decimelo")
            interactivo = 0
            break

        except (ValueError):
            print("Ooops, ingresa 1 o 0, o al menos un numero flaco")            

    if interactivo == 1:
        modo_interactivo = True
        print(" ")
    else:
        modo_interactivo = False

    #Modo interactivo on
    while modo_interactivo == True: 
        sleep(0.3)
        print("Modificar una tarea -> 1")
        print("Agregar una tarea -> 2")
        print("Eliminar una tarea -> 3")
        print("Salir -> 4")
        while True:
            try:  
                accion = int(input("Opcion: "))
                if accion == 1 or accion == 2 or accion == 3 or accion == 4:
                    break
                else:
                    print("1, 2, 3, 0 4 manin")
            except(ValueError): 
                print("amigo un numero te pido (1, 2, 3, o 4)")
        sleep(0.3)

        if accion == 4: 
            modo_interactivo = False



        #Modificar tareas
        while accion == 1: 
            sleep(0.3)
            file = open("/home/luciowo/scripts_inicio/tareas.txt", 'w+')
            print("¿Que tarea queres modificar? (-1 para cancelar)")
            for i in range(len(cant_lineas)): 
                print("Tarea","-",i + 1)

            while True: 
                try: 
                    n = int(input("Numero de tarea: "))
                    if n > 0 and n <= len(cant_lineas) or n == -1:
                        break
                    else: 
                        print("ingresa un numero de tarea valido por favor ")
                except(ValueError):
                    print("Que barbaro lo tuyo ") 
            #cancelar modificar tareas
            if n == -1: 
                file.close()
                break

            while True:
                try:
                    string = str(input("Modifica la tarea (ingresa texto) "))
                    break
                except(ValueError): 
                    print("Hay que ser bastante creativo para hacer disparar esta excepcion")

            cant_lineas[n - 1] = (string + '\n') 
            file.writelines(cant_lineas)
            print("Tarea",n, "modificada, ahora es:", cant_lineas[n -1])

            while True:
                try: 
                    accion = int(input("Queres modificar otra tarea (1) o seguir (0)? "))
                    if accion == 0 or accion == 1: 
                        file.close()
                        break
                    else: 
                        print("Por favor ingresa 1 o 0 para continuar putito rico ")
                except(ValueError): 
                    print("1 o 0, 1 o 0, 1 o 0, 1 o 0, 1 o 0, 1 o 0 ")



        #Agregar tareas
        while accion == 2:
            sleep(0.3) 
            file = open("/home/luciowo/scripts_inicio/tareas.txt", 'w+')
            new_task = str(input("Agrega tu nueva tarea! (-1 para cancelar) "))
            if new_task == '-1': 
                file.close()
                break
            
            cant_lineas.append(new_task + '\n')
            file.writelines(cant_lineas)

            for i in range(len(cant_lineas)): 
                print("Tarea","-",i + 1, cant_lineas[i])

            while True: 
                try:
                    agregar = int(input("Agregar mas tareas(1) o continuar(0)? "))

                    if agregar == 1 or agregar == 0: 
                        break
                except(ValueError): 
                    print("Se te perdio el 1?")
            
            if agregar == 1:
                accion = 2
            else: 
                file.close()
                accion  = 4
                 


        #Eliminar tareas 
        while accion == 3: 
            file = open("/home/luciowo/scripts_inicio/tareas.txt", 'w+')
            print(" ")
            print("Tareas a elegir, 1 ->",len(cant_lineas),"(0 para finalizar)")
            while True: 
                try:
                    eliminar = int(input("Opcion: "))
                    if eliminar >= 0 and eliminar <= len(cant_lineas):
                        break
                    else: 
                        print("Ingresa un numero entre 1 y", len(cant_lineas)," ")
                except(ValueError): 
                    print("Complicado contar no? ")
            if eliminar == 0: 
                file.close()
                break
            while True:
                try:
                    confirm = int(input("Seguro? 1 -> si, 0 -> no " ))
                    if confirm == 1 or confirm == 0: 
                        break
                    else: 
                        print("1 o 0 papi")
                except(ValueError): 
                    print("Dale vos podes tipear un 1 o 0 ")
            if confirm == 1: 
                cant_lineas.pop(eliminar - 1)
                for i in range (len(cant_lineas)):
                    print(i + 1,"-",cant_lineas[i]) 
                file.writelines(cant_lineas)
            else: 
                while True: 
                    try: 
                        eliminar = int(input("Eliminar otra tarea?(1) o finalizar (0)? "))
                        if eliminar == 1 or eliminar == 0:
                            break
                        else:
                            print("1 o 0 flaco")
                    except(ValueError):
                        print("Si eso es un 1 o 0 para vos, estamos complicados ")
                if eliminar == 0: 
                    file.close()
                print(" ")



if __name__ == '__main__':
    main()
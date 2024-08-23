from time import sleep
import os # Este módulo provee una manera versátil de usar funcionalidades dependientes del sistema operativo.
import signal

class TimeoutException(Exception): 
    pass

#raise: levantaz/alzar/subir; used to throw (or raise) an exception
def timeout_handler(signum, frame):
    raise TimeoutException

def main():
    #Inicio, lectura de archivo.txt
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
    try:
        signal.alarm(10)  # Tiempo límite de 10 segundos
        interactivo = int(input("Elige una opción: "))
        signal.alarm(0)  # Cancelar alarma si se responde a tiempo
    except TimeoutException:
        print("\nTiempo agotado. Asumiendo respuesta negativa.")
        interactivo = 0

    while interactivo != 1 and interactivo != 0:
        interactivo = int(input("Por favor ingresa 1 o 0 para continuar putito rico "))
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
        accion = int(input("Opcion: "))
        
        while accion != 1 and accion != 2 and accion != 3 and accion != 4: 
            sleep(0.3)
            accion = int(input("Por favor ingresa 1, 2, 3 o 4. putito rico "))

        if accion == 4: 
            modo_interactivo = False

        #Modificar tareas
        while accion == 1: 
            sleep(0.3)
            file = open("/home/luciowo/scripts_inicio/tareas.txt", 'w+')
            print("¿Que tarea queres modificar?")
            for i in range(len(cant_lineas)): 
                print("Tarea","-",i + 1)

            n = int(input("Numero de tarea: "))
            string = str(input("Modifica la tarea (ingresa texto) "))

            cant_lineas[n - 1] = (string + '\n') 
            file.writelines(cant_lineas)
            print("Tarea",n, "modificada, ahora es:", cant_lineas[n -1])

            accion = int(input("Queres modificar otra tarea (1) o seguir (0)? "))
            if accion == 0: 
                file.close()
            while accion != 1 and accion != 0: 
                M = int(input("Por favor ingresa 1 o 0 para continuar putito rico "))
            
        #Agregar tareas
        while accion == 2:
            sleep(0.3) 
            file = open("/home/luciowo/scripts_inicio/tareas.txt", 'w+')
            new_task = str(input("Agrega tu nueva tarea! "))
            cant_lineas.append(new_task + '\n')
            file.writelines(cant_lineas)

            for i in range(len(cant_lineas)): 
                print("Tarea","-",i + 1, cant_lineas[i])
            agregar = int(input("Agregar mas tareas(1) o continuar(0)? "))

            while agregar != 1 and agregar != 0: 
                agregar = int(input("Por favor ingresa 1 o 0 para continuar putito rico "))
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
            eliminar = int(input("Opcion: "))
            while eliminar < 0 or eliminar > len(cant_lineas):
                eliminar = int(input("Ingresa un numero entre 1 y", len(cant_lineas)," "))
            if eliminar == 0: 
                break
            confirm = int(input("Seguro? 1 -> si, 0 -> no " ))
            if confirm == 1: 
                cant_lineas.pop(eliminar - 1)
                for i in range (len(cant_lineas)):
                    print(i + 1,"-",cant_lineas[i]) 
                file.writelines(cant_lineas)
            else: 
                eliminar = int(input("eliminar otra tarea?(1) o finalizar (0)? "))
                if eliminar == 0: 
                    file.close()
                print(" ")

if __name__ == '__main__':
    main()
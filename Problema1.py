# ==============================================================================
# Curso: Fundamentos de Programación (Código: 213022)
# Fase 5 - Evaluación Final POA
# Problema 1
# ==============================================================================

# Empezamos definiendo la funcion para calcular los perimetros que pide el ejercicio
def calcular_clasificacion(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"
    
#funcion principal para reguistrar y analizar cada cliente
def main():
    print("==================================================")
    print("       SISTEMA DE EVALUACIÓN DE COMPROMISO        ")
    print("==================================================")
    #Matriz vacia donde almacenaremos los datos de las sesiones
    matriz_sesiones = []
    
    #Contador para llevar el número de sesiones registradas
    contador = 1
    
    #Bucle para registrar múltiples sesiones hasta que el usuario decida detenerse
    while True:
        print(f"\n--- Registrando Sesión #{contador} ---")
        
        id_cliente = input("ID del Cliente: ").strip()
        #para evitar que la ID quede vacia
        if not id_cliente:
            print("El ID del cliente no puede estar vacío. Por favor, ingrese un ID válido.")
            continue
        
        #solicita los datos de los parametros 
        while True:
            try:
                duracion = int(input("Duración de la Sesión (en segundos): "))
                if duracion >= 0:
                    break
                #cada una tiene su mensaje de error para evitar que el usuario ingrese datos no validos, ambas son iguales
                print("La duración no puede ser negativa. Por favor, ingrese un valor válido.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número entero para la duración.")
        while True:
            try:
                clics = int(input("Número de Clics: "))
                if clics >= 0:
                    break
                print("El número de clics no puede ser negativo. Por favor, ingrese un valor válido.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número entero para los clics.")
        
        #Una vez que tenemos los datos validos, los almacenamos en la matriz de sesiones
        matriz_sesiones.append([id_cliente, duracion, clics])
        print("\nDatos registrados con éxito.\n")
        
        #Añadimos uno al contador al final de cada registro
        contador += 1
        
        #Preguntamos al usuario si desea registrar otra sesión
        respuesta = input("¿Desea registrar otra sesión? (si/no): ").strip().lower()
        
        if respuesta in ["si", "s"]:
            continue
        elif respuesta in ["no", "n"]:
            break
        #Si el usuario ingresa una respuesta no válida, también finalizamos el registro de sesiones
        else:
            print("\nRespuesta no válida. Finalizando el registro de sesiones.")
            break
        
    #Una vez que el usuario ha terminado de registrar las sesiones, procedemos a analizar los datos y generar el informe final
    matriz_informe = []
    #Recorremos cada sesión registrada en la matriz de sesiones, calculamos la clasificación para cada cliente y almacenamos el resultado en la matriz de informe
    for sesion in matriz_sesiones:
        id_clie = sesion[0]
        dur_seg = sesion[1]
        num_clic= sesion[2]
        
        #Llamamos a la función calcular_clasificacion para obtener la clasificación final del cliente según los parametros 
        resultado_final = calcular_clasificacion(dur_seg, num_clic)
        #Luego almacenamos el resultado en la matriz de informe junto con el ID del cliente
        matriz_informe.append([id_clie, resultado_final])
        
    print("\n==================================================")
    print("          INFORME FINAL DE COMPROMISO             ")
    print("==================================================")
    print(f"{'ID CLIENTE':<20} | {'CLASIFICACIÓN FINAL'}")
    print("-" * 48)
    #Finalmente, recorremos la matriz de informe para imprimir el ID de cada cliente junto con su clasificación final, utilizando un formato alineado para una mejor presentación
    for fila in matriz_informe:
        print(f"{fila[0]:<20} | {fila[1]:<20}")
        
if __name__ == "__main__":
    main()

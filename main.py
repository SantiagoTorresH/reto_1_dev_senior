import datetime

'''Atributos de un experimento:nombre, fecha, tipo, resultados numericos'''

listaDeExperimentos = [
    # ["Esperimento 1", "16/11/2024", "Quimica",[5,2,3,56,7]]
]


#listaDeExperimentos2 = []

def agregar_experimetos():
    nombre = input("Vas a agregar un experimento \n ingrese el nombre del experimento:")
    
    fecha = input("Ingrese la fecha de ralizacion, (DD/MM/YYYY): ")
    try:
        datetime.datetime.strptime(fecha, "%d/%m/%Y") # si lo hace bien es un try, si no except
        #asifna lo de str a fechalimite 
    except ValueError:
        print("Fecha no valida.")
        return # vuelve y lo retorna para que ingrese 
    
    categoria = input('Ingrese la categoria, puede ser "Quimica", "fisica" o "Biologia": ').capitalize()
    
    # Asegurarse de que la categoría esté entre las opciones permitidas
    while categoria not in ["Quimica", "Fisica", "Biologia"]:
        print("Categoría no válida. Por favor ingrese una de las siguientes: 'Quimica', 'Fisica' o 'Biologia'.")
        categoria = input('Ingrese la categoría, puede ser "Quimica", "Fisica" o "Biologia": ').capitalize()


    resultados = input("Ingrese los resultados obtenidos separados por comas, ej(4, 5.1, 7.4) : ")  # 5, 4,3 
    try:
        #resultados = [int(x) for x in resultados.split(",")]    # Convierte la entrada a una lista de enteros
        resultados = list(map(float, resultados.split(",")))     # separa con comas los numeros que ingreso, se le pasa que es float, el map sefara lo que aparentemente era flotante y lo convierte en una lista separadas por comas. 
    # antes del map todo era un solo numero, el map los coge y separa cada numero y los agrega a la lista. 
    except ValueError:
        print(" no valida.")    
        return
    
    listaDeExperimentos.append([nombre,fecha,categoria, resultados])
    print("Experimento agregado exitosamente.")
    
    


def eliminar_experimentos():
    """Perminte eliminar un experimento. dificultad: 1, requiere el uso de la funcion agregar_experimento"""
    
    pass


def visualizar_experimentos():
    """Permite visualizar todos los experimentos. dificultad: 1. requiere el uso de la funcion agregar_experimento"""
    if not listaDeExperimentos:
        print("No hay experimentos disponibles para mostrar.")
        return  # Salir de la función si no hay experimentos

    # Si hay experimentos, se recorren y se muestran sus detalles
    print("Lista de experimentos:")
    for exp in listaDeExperimentos:
        nombre, fecha, categoria, resultados = exp
        # Imprimir los detalles del experimento
        print(f"\nNombre: {nombre}")
        print(f"Fecha: {fecha}")
        print(f"Categoría: {categoria}")
        print(f"Resultados: {resultados}")
        

def calcular_Estadisticas():
    """Calcular estadisticas basicas(promedios, máximos y mínimos) de un experimento. dificultad: 2. requiere el uso de funcion agregar_experimento"""
    pass

def comparar_experimentos():
    '''compara dos o mas experimentos para determinar los mejores o peores resultados'''

def generar_informe():
    """Generar un informe resumen de los expremintos y sus estadisticas. dificultad: 3. requiere el uso de funciones visualizar_experimentos y calcular_estadisticas"""
    
    pass

def mostrar_menu():
    print("===Menu Principal====")
    
    print("===Gestion de experimentos====")
    print("1. Agregar experimento")
    print("2. Visualizar experimentos")
    print("3. Eliminar experimentos")
    
    print("===Analisis de datos====")
    print("4. calcular estadisticas ")
    print("5. comparar experimentos ")
    
    print("===Informes====")
    print("6. generar Informe")
    print("====Salir====")
    print("7. Salir")
    
    
def main():
    """Controla el flujo general del sistema. dificultad: 1"""
    mostrar_menu()   
    while True: 
        opcion  = input("Seleccione una opcion: ")
        if opcion == "1":
            agregar_experimetos()
        elif opcion == "2":
            visualizar_experimentos()
        elif opcion == "3":
            eliminar_experimentos()
        elif opcion == "4":
            calcular_Estadisticas()
        elif opcion == "5":
            comparar_experimentos()
        elif opcion == "6":
            generar_informe()
        elif opcion == "7":
            print("Saliendo del programa")   
            break
        else:
            print("Ingrese una opcion valida")             
            

main()


# if __name__ == "__main__":  # es lo mismo al main pero mas avanzado, 
#     main()



    
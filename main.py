import datetime
import statistics

'''Atributos de un experimento:nombre, fecha, tipo, resultados numericos'''

experimentsList = [
    ["Experimento 1", "16/11/2024", "Quimica", [5,2,3,56,7]],
]


#listaDeExperimentos2 = []

def append_experiments():
    name = input("Vas a agregar un experimento \n ingrese el nombre del experimento:")
    
    date = input("Ingrese la fecha de ralizacion, (DD/MM/YYYY): ")
    try:
        datetime.datetime.strptime(date, "%d/%m/%Y") # si lo hace bien es un try, si no except
        #asifna lo de str a fechalimite 
    except ValueError:
        print("Fecha no valida.")
        return # vuelve y lo retorna para que ingrese 
    
    category = input('Ingrese la categoria, puede ser "Quimica", "fisica" o "Biologia": ').capitalize()
    
    # Asegurarse de que la categoría esté entre las opciones permitidas
    while category not in ["Quimica", "Fisica", "Biologia"]:
        print("Categoría no válida. Por favor ingrese una de las siguientes: 'Quimica', 'Fisica' o 'Biologia'.")
        category = input('Ingrese la categoría, puede ser "Quimica", "Fisica" o "Biologia": ').capitalize()

    results = input("Ingrese los resultados obtenidos separados por comas, ej(4, 5.1, 7.4) : ")  # 5, 4,3 
    try:
        #resultados = [int(x) for x in resultados.split(",")]    # Convierte la entrada a una lista de enteros
        results = list(map(float, results.split(",")))     # separa con comas los numeros que ingreso, se le pasa que es float, el map sefara lo que aparentemente era flotante y lo convierte en una lista separadas por comas. 
    # antes del map todo era un solo numero, el map los coge y separa cada numero y los agrega a la lista. 
    except ValueError:
        print(" no valida.")    
        return
    
    experimentsList.append([name,date,category, results])
    print("Experimento agregado exitosamente.")
    
    


def delete_experiments():
    """Perminte eliminar un experimento. dificultad: 1, requiere el uso de la funcion agregar_experimento"""
    if not experimentsList:
        print("No hay experimentos para eliminar.")
        return
    
    nameToDelete = input("Ingrese el nombre del experimento que desea eliminar:")
    #Busco en la lista ese nombre
    for exp in experimentsList:
        if exp[0].lower() == nameToDelete.lower():
            experimentsList.remove(exp)
            print(f"El experimento '{nameToDelete}' ha sido eliminado exitosamente. ")
            return
    print(f"No se encontro el experimento '{nameToDelete}'")    
    
    
    pass


def view_experiments():
    """Permite visualizar todos los experimentos. dificultad: 1. requiere el uso de la funcion agregar_experimento"""
    if not experimentsList:
        print("No hay experimentos disponibles para mostrar.")
        return  # Salir de la función si no hay experimentos

    # Si hay experimentos, se recorren y se muestran sus detalles
    print("Lista de experimentos:")
    for exp in experimentsList:
        name, date, category, results = exp
        # Imprimir los detalles del experimento
        print(f"\nNombre: {name}")
        print(f"Fecha: {date}")
        print(f"Categoría: {category}")
        print(f"Resultados: {results}")
        

def calculate_Statictics():
    """Calcular estadisticas basicas(promedios, máximos y mínimos) de un experimento. dificultad: 2. requiere el uso de funcion agregar_experimento"""

    if not experimentsList:
        print("No hay experimentos para calcular estadísticas.")
        return
    
    for exp in experimentsList:
        name, date, category, results = exp  
        
        if results:
            try:
                average = statistics.mean(results) # halla el promedio
                max_value = max(results) # maximo
                min_value = min(results) # minimo
                
                print(f"\n Estadisticas para el experimento '(name)': ")
                print(f"Promedio: {average:.2f} ")
                print(f"Maximo: {max_value} ")
                print(f"Minimo: {min_value} ")
            except statistics.StatisticsError:
                print(f"No se pueden calcular estadísticas para el experimento '{name}' (sin resultados).")
        else:
            print(f"No se pueden calcular estadísticas para el experimento '{name}' (sin resultados).")            
                
                

def compare_Experiments():
    '''compara dos o mas experimentos para determinar los mejores o peores resultados'''
    if len(experimentsList) < 2:
        print("No hay suficientes experimentos para comparar.")
        return
    # Ver lista de experimentos
    print("Lista de experimentos disponibles para comparar:")
    for i, exp in enumerate(experimentsList, start=1):
        name, date, category, results = exp
        print(f"{i}. {name}")
    
    # Seleccionar experimentos para comparar
    indices = input("Ingrese los números de los experimentos que desea comparar, separados por comas (ej. 1, 2, 3): ")
    try:
        selected_indices = list(map(int, indices.split(",")))
        # Validar que los índices ingresados sean correctos
        selected_experiments = []
        for index in selected_indices:
            if index < 1 or index > len(experimentsList):
                print(f"Índice {index} no es válido.")
                return
            selected_experiments.append(experimentsList[index - 1])  # -1 para ajustar el índice
    except ValueError:
        print("Entrada no válida. Asegúrese de ingresar números separados por comas.")
        return
    
    # Comparar los experimentos seleccionados
    best_avg_exp = None
    best_max_exp = None
    best_min_exp = None
    best_avg = -float('inf')
    best_max = -float('inf')
    best_min = float('inf')
    
    for exp in selected_experiments:
        name, date, category, results = exp
        if results:
            avg = statistics.mean(results)
            max_value = max(results)
            min_value = min(results)
            
            # Determinar el experimento con el mejor promedio
            if avg > best_avg:
                best_avg = avg
                best_avg_exp = name
            
            # Determinar el experimento con el valor máximo más alto
            if max_value > best_max:
                best_max = max_value
                best_max_exp = name
            
            # Determinar el experimento con el valor mínimo más bajo
            if min_value < best_min:
                best_min = min_value
                best_min_exp = name
        else:
            print(f"No se pueden comparar resultados para el experimento '{name}' (sin resultados).")
    
    # Mostrar los resultados de la comparación
    print("\nResultados de la comparación:")
    
    if best_avg_exp:
        print(f"El experimento con el mejor promedio es '{best_avg_exp}' con un promedio de {best_avg:.2f}")
    if best_max_exp:
        print(f"El experimento con el mayor valor máximo es '{best_max_exp}' con un valor máximo de {best_max}")
    if best_min_exp:
        print(f"El experimento con el menor valor mínimo es '{best_min_exp}' con un valor mínimo de {best_min}")

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
            append_experiments()
        elif opcion == "2":
            view_experiments()
        elif opcion == "3":
            delete_experiments()
        elif opcion == "4":
            calculate_Statictics()
        elif opcion == "5":
            compare_Experiments()
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



    
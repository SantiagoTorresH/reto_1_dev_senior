# Reto 1 Dev Senior: Phyton 🐍

## Simulacion de un Proyecto de Investigacion Científica en Python 🐍

El presente repositorio corresponde al desarrollo de las actividades propuestas en el reto #1 del curso de Python y Dev Senior. Los autores somos **Santiago Torres** y **Lindsey Acourtt**. 

El objetivo de este proyecto es desarrollar una aplicación basada en consola, enfocada en la recopilación, análisis y manipulación de datos científicos.

### Menú principal. 

Una vez el usuario inicia el programa, se le presentará el siguiente menú. El usuario debe ingresar el número de la función que desea llevar a cabo. Si ingresa algo diferente al número de una de las funciones disponibles, el usuario tendrá que intentarlo de nuevo. 

El detalle de cada función se detalla en la siguiente sección. 

```
===Main Menu====
===Management of experiments====
1. Add an experiment
2. View experiments
3. Delete an experiment
===Analysis of data====
4. Calculate statistics         
5. Compare experiments 
===Reports====
6. Generate a report
====Exit====
7. Exit
Select an option:
```


### Funciones del programa🔍

#### 1. Recopilación de datos experimentales

El programa le permite al usuario registrar, visualizar y elimnar experimentos. Cada operación se realiza en tres funciones diferentes:

* ```addExperiment```: Permite agregar un experimento. Cada experimento se crea como instancia de una clase, y está definido por los siguientes atributos:📅
    * **Nombre del experimento**. Puede ser cualquier nombre deseado por el usuario.
    * **Fecha de realización del experimento**. Debe ser ingresada en el formato dd/mm/aaaa. Se ha escrito esta función de tal modo que permita verificar que el usuario ingresó la fecha en el formato correcto.
    * **Categoría**. Esta es predefinida, el usuario solo puede ingresar una de las tres categorías (química, física o biología). Si se ingresa una categoría diferente, el usuario tendrá que volver a intentarlo.
    * **Resultados**. Se pueden ingresar un mínimo de 3 resultados, y un máximo de 10. Los resultados deben ser numéricos. Se realizan verificaciones que aseguran que el usuario ingrese un número. Si el usuario se equivoca, recibirá el mensaje, y tendrá que intentarlo de nuevo.
* ```printExperiments```: Permite al usuario visualizar todos los experimentos registrados hasta el momento. Si no hay experimentos registrados, se le indicará al usuario, y se regresará al menú principal. 
* ```removeExperiment```: Se puede eliminar experimentos a través de esta función. Solo se permite eliminar una a la vez. Si no hay experimentos en la lista de experimentos, se le mostrará esta información al usuario y será retornado al menú principal. Para eliminar un experimento, el usuario debe ingresar el número del experimento en la lista de experimentos registrados. Si el usuario no recuerda cuál es el número en la lista del experimento a eliminar, tiene la opción de visualizar una lista resumida del número y el nombre de los experimentos disponibles. 

#### 2. Análisis de resultados experimentales.

El programa le permite al usuario realizar un análisis básico de los datos experimentales que ha ingresado. Se utilizan las siguientes funciones para ello:

* ```calculateStatistics```: El usuario puede escoger un experimento de entre la lista de experimentos registrados para calcular el promedio de los datos, el valor mínimo, y el valor máximo. Si no hay experimentos registrados, se le indicará al usuario. Al igual que con la función eliminar, para seleccionar un experimento para analizarlo, el usuario debe ingresar el número del experimento en la lista de experimentos registrados. Si el usuario no recuerda cuál es el número en la lista del experimento a analizar, tiene la opción de visualizar una lista resumida del número y el nombre de los experimentos disponibles.
* ```compareExperiments```: El usuario puede escoger dos o más experimentos. A cada uno se le calcula el promedio, el valor mínimo y el valor máximo, luego el programa muestra cuál de los experimentos seleccionados para comparar tiene mayor y menor promedio, mayor y menor valor mínimo y mayor y menos valor máximo. Si no hay experimentos registrados, esto se le indicará al usuario, y si solo hay un experimento, se le indicará también, avisando que no hay experimentos suficientes para realizar una comparación. Similar que con las funciones eliminar y calcular estadísticas, el usuario debe ingresar el número del experimento en la lista para escoger qué experimentos quiere comparar, si no lo recuerda, tiene la opción de mostrar la lista resumida de los experimentos. A medida que el usuario va ingresando los números, se va mostrando una lista de los experimentos seleccionados. 

#### 3. Generación de reporte

Para generar el reporte, se utiliza la sigueinte función:  

* ```generateReport```: El programa le permite al usuario generar un archivo .txt en donde se muestre la lista de los experimentos registrados. Además, el reporte incluye una comparación del análisis de los datos de todos los resultados, especificando qué experimento tuvo el promedio más alto y más bajo, el valor mínimo más alto y más bajo, y el valor máximo más alto y más bajo.

A continuación, se presenta un ejemplo de cómo es el resultado de dicho reporte. 

```
-------------------
LIST OF EXPERIMENTS
-------------------

----- Experiment #: 1 -----
Name: Erlenmeyer Flask's calibration
Date: 2024-03-17
Category: Chemistry
Results: [200.13, 201.01, 198.99, 199.5, 200.03]
The average is: 199.93
The minimum value is: 198.99
The maximum value is: 201.01

----- Experiment #: 2 -----
Name: Water with salt's boiling point
Date: 2024-11-13
Category: Chemistry
Results: [106.9, 105.8, 106.3]
The average is: 106.33
The minimum value is: 105.8
The maximum value is: 106.9

----- Experiment #: 3 -----
Name: Refractive index of a diamond
Date: 2024-10-23
Category: Physics
Results: [2.37, 2.4, 2.42, 2.6, 2.1, 2.45]
The average is: 2.39
The minimum value is: 2.1
The maximum value is: 2.6

----- Experiment #: 4 -----
Name: Gravity's strength
Date: 2024-07-04
Category: Physics
Results: [10.01, 9.98, 9.83, 9.9]
The average is: 9.93
The minimum value is: 9.83
The maximum value is: 10.01

----- Experiment #: 5 -----
Name: Newborn babies weight
Date: 2024-09-05
Category: Biology
Results: [2730.0, 3600.0, 2540.0, 4190.0, 4400.0, 3250.0, 2980.0, 3010.0, 4004.0, 3540.0]
The average is: 3424.40
The minimum value is: 2540.0
The maximum value is: 4400.0

----- Experiment #: 6 -----
Name: Newborn babies length
Date: 2024-05-09
Category: Biology
Results: [50.1, 49.34, 48.2, 53.1, 49.2, 48.94, 46.36, 51.04, 48.67, 49.0]
The average is: 49.40
The minimum value is: 46.36
The maximum value is: 53.1

-------------------------------
COMPARISION BETWEEN EXPERIMENTS
-------------------------------

--------------------
Comparision of mean:
--------------------
Highest average: Experiment #5 with a value of 3424.40
Lowest average: Experiment #3 with the value of 2.39
----------------------------
Comparision of minimum value:
----------------------------
Highest Min Value: Experiment #5 with a value of 2540.0
Lowest Min Value: Experiment #3 with the value of 2.1
-----------------------------
Comparision of maximum value:
-----------------------------
Highest Max Value: Experiment #5 with a value of 4400.0
Lowest Max Value: Experiment #3 with the value of 2.6
```

#### 4. Generación de reporte

Funciones secundarias. Se utilizan las siguientes funciones para apoyar el desarrollo del programa:

* ```displayExperimentsName```: Es similar a ```printExperiments```, pero solo imprime el nombre de los experimentos registrados y su número asignado en la lista. Se usa en medio de las operaciones de eliminación, análisis y comparación, para recordarle al usuario cuáles son los experimentos disponibles en caso de que no recuerde cuál es el experimento que desea seleccionar.
* ```userMenu```: Imprime el menú de opciones al usuario, es el menú principal.

### Librerías usadas

Las librerías usadas son:

* ```datetime```: Esta permite la creación de objetos datetime, date o time. Se ha utilizado específicamente para el formato de las fechas de realización de los experimentos, las cuales se manejan como objetos "date".
* ```statistics```: Se utiliza para el análisis de los resultados de los experimentos que ingresa el usuario. Se usa para calcular el promedio de los resultados de los experimentos.

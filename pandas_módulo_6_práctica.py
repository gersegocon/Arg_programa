
"""Pandas_Módulo_6_Práctica.ipynb
---
# ***Argentina Programa 4.0 - Programación Avanzada con Python***
---

## **Módulo 6**: Librería Pandas - Práctica

### ***Universidad Nacional de Chilecito***

---

## Dataset

El dataset que usaremos es una versión muy resumida de datos de la Encuesta Permanentes de Hogares (relevamiento llevado adelante por el INDEC). Se trata de una encuesta continua que tiene como objetivo fundamental generar información sobre el funcionamiento del mercado de trabajo.

Solamente utilizaremos algunas variables (edad, nivel educativo, cantidad de horas trabajadas, calificación de la tarea e ingreso laboral) y algunos casos (los ocupados, es decir, aquellos que han trabajado al menos una hora en la semana anterior al relevamiento).

Este dataset es el mismo que emplearemos en la clase presencial, y en estos ejercicios buscamos  familiarizarnos con él y revisar algunos temas.

## Ejercicio 1

Busquemos en la documentación de pandas la sintaxis del método `read_csv` y leamos en un `DataFrame` llamado data los datos del archivo /Data/data_filt.csv

Este archivo tiene algunos datos numéricos y otros de tipo cadena de caracteres.

Las columnas son:

* ch06: int, edad

* nivel_ed: string, nivel educativo

* htot: int, cantidad de horas totales trabajadas en el período

* calif: string, calificación de la tarea

* p47t: int, ingreso

Con ayuda del siguiente código podrás vincular tu cuenta de Google Drive.
Como recomendación te pedimos que crees una carpeta denominada como `AP_UNdeC` dentro de tu carpeta principal de Drive.
Dentro de esa carpeta crea otra carpeta denominada `Data` en esa carpeta deberás subir siempre los archivos que necesites utilizar.
"""

from google.colab import drive
drive.mount('/content/drive')
pathCurso = '/content/drive/MyDrive/AP_UNdeC/Data/'

"""Con el siguiente comando podrás abrir el archivo que vamos a necesitar en ésta ocasión:"""

import numpy as np

# local:
data_location = pathCurso + 'data_filt.csv'

"""Importamos la biblioteca pandas y asignamos pd como alias:"""

import pandas as pd

"""Con el siguiente código podrás importar el archivo:"""

data = pd.read_csv(data_location, sep=",", encoding="latin1")
data.head(3)

"""## Ejercicio 2

Miremos ahora los primeros tres registros del `DataFrame` data, y los ultimos cinco registros.

¿Cuántas filas tiene data? ¿Y cuántas columnas?

Ayudas:

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html?highlight=head#pandas.DataFrame.head

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.tail.html?highlight=tail#pandas.DataFrame.tail

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.shape.html?highlight=shape#pandas.DataFrame.shape

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.info.html?highlight=info

"""

display(data.head(3))
print("")
print("--------------")
display(data.tail())
print("")
print("--------------")
print("FILAS",data.shape[0])
print("COLUMNAS",data.shape[1])

"""## Ejercicio 3

¿Cuáles son los nombres de las columnas del `DataFrame` data?

¿Cuál es el índice del `DataFrame` data?

Ayudas:

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.columns.html?highlight=columns#pandas.DataFrame.columns

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.index.html?highlight=index#pandas.DataFrame.index

"""

display(data.columns)
display(data.index)

"""Renombremos ahora los columnas para que queden con estos valores:

['edad', 'nivel_educativo', 'hs_trabajados', 'calif_ocupacional', 'ingreso_ult_mes']
"""

data.columns =['edad', 'nivel_educativo', 'hs_trabajados', 'calif_ocupacional', 'ingreso_ult_mes']
data

"""## Ejercicio 4

¿Cuál es el tipo de datos de la cuarta columna de data?
"""

display(data.iloc[:,3])
data.iloc[:,3].dtype

"""## Ejercicio 5

¿Cómo están distribuidos los niveles educativos? ¿Cuál es el más común?

Ayuda:

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html?highlight=value_counts#pandas.Series.value_counts

"""

print(data['nivel_educativo'].unique())
data['nivel_educativo'].value_counts()

"""## Ejercicio 6

¿Cuál es el ingreso medio de la población?
"""

data['ingreso_ult_mes'].mean()

"""## Ejercicio 7

Construyamos un objeto `DataFrame` con las columnas nivel_educativo e ingreso_ult_mes de data

Seleccionemos las primeras 20 filas de este objeto `DataFrame`

Seleccionemos una muestra aleatoria de 500 filas de este objeto `DataFrame`

Ayuda:

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html?highlight=sample#pandas.DataFrame.sample
"""

data2 = data[['nivel_educativo','ingreso_ult_mes']]
display(data2.head(20))
print("")
print("---------------")
display(data2.sample(500))

"""## Ejercicio 8

Construyamos un objeto `DataFrame` con todas las columnas de data excluyendo nivel_educativo.

Ayuda:

Construir una máscara booleana de los nombres de las columnas.

"""

mascara = data.columns != 'nivel_educativo'
data3 = data.loc[:, mascara]

print(data3)

"""## Ejercicio 9

Ordenar data según la columna edad en forma decreciente.

Ayuda:

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html?highlight=sort_values#pandas.DataFrame.sort_values

"""

data.sort_values('edad',ascending=False)

"""## Ejercicio 10

¿Cuál es el promedio de horas trabajadas de los jóvenes entre 14 y 25 años y poco calificados?

Ayuda:
    
Combina varias máscaras booleanas
"""

mask1 = (data['edad'] >= 14) & (data['edad'] <= 25)
mask2 = (data['calif_ocupacional'] == '2_Op./No calif.')

data4 = data.loc[mask1 & mask2]
print('Promedio de horas trabajadas: ',round((data4['hs_trabajados'].mean()),2)," horasss")

"""## Ejercicio 11

Generemos un nuevo dataframe con los trabajadores que ganan más del promedio de ingresos general y están por debajo de la cantidad media de horas trabajadas. ¿Cuántos trabajadores se encuentran en esta condición? ¿Cuál es su edad mediana?

Ayuda:

Calcular el promedio de ingresos y la media de horas trabajadas

Construir máscaras booleanas con estos valores

Indexar data con la combinación de las máscaras construidas

"""

mask3 = data['ingreso_ult_mes'] > data['ingreso_ult_mes'].mean()
mask4 = data['hs_trabajados'] < data['hs_trabajados'].mean()

data5 = data.loc[mask3 & mask4]
print("Total de trabajadores en condición: ",len(data5))
print("Edad mediana: ",data5['edad'].median())
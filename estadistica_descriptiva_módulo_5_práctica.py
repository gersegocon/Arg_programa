"""Estadistica_Descriptiva_Módulo_5_Práctica.ipynb
---
# ***Argentina Programa 4.0 - Programación Avanzada con Python***
---

## **Módulo 5**: Estadística Descriptiva - Práctica

### ***Universidad Nacional de Chilecito***

---

La idea de esta práctica es ejercitar los puntos que vamos a necesitar para resolver el desafío.

Usaremos un resumen del dataset de Kaggle que tiene datos de ventas:

https://www.kaggle.com/kyanyoga/sample-sales-data

## Ejercicio 1
Leer los datos del archivo /Data/sales_data_sample_excercise.csv

Este archivo tiene algunos datos numéricos y otros de tipo cadena de caracteres.

Las columnas son:

* ORDERNUMBER: int, id de la orden

* SALES: float, monto abonado

* MONTH_ID: int, mes

* YEAR_ID: int, año

* PRODUCTLINE: str, producto

* COUNTRY: str, país de venta

¿Recuerdan que todos los elementos de una instancia de ndarray deben ser del mismo tipo? Entonces vamos a leer el archivo y crear una instancia de ndarray de tipo cadena de caracteres.

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
data_location = pathCurso + 'sales_data_sample_excercise.csv'

"""Con el siguiente código podrás importar el archivo:"""

data = np.genfromtxt(data_location, skip_header=1, delimiter='\t', dtype= str)
data

data_type_str = np.genfromtxt(data_location, skip_header=1, delimiter='\t', dtype= str)
data_type_str

data_type_int = np.genfromtxt(data_location, skip_header=1, delimiter='\t', dtype= int)
data_type_int

data_type_float = np.genfromtxt(data_location, skip_header=1, delimiter='\t', dtype= float)
data_type_float

"""## Ejercicio 2

La función `distribution_plotter` grafica los datos que recibe como parámetro en una instancia de numpy array

Graficar los precios de ventas en tres países. ¿Qué pueden decir respecto a sus distribuciones?

Comparar las distribuciones con la de los precios de ventas sin distinguir por paises
"""

import seaborn as sns

def distribution_plotter(data, label, bin_width=500):
    sns.set(rc={"figure.figsize": (7, 5)})
    sns.set_style("white")
    dist = sns.histplot(data, stat = 'count', kde = False,
                        line_kws = {'linewidth':5},
                        binwidth = bin_width)
    dist.set_title('Distribucion: ' + label + '\n', fontsize = 16)



"""Con ayuda del siguiente comando podrás ver que pasíses hay:"""

country_vector = data[:, 5]

paises_unicos = np.unique(country_vector)
print(paises_unicos)

sales = data_type_float[:,1]
country = data_type_str[:,5]

mask = country == "Germany"
sales_germany = sales[mask]

distribution_plotter(sales_germany, "Ventas Alemania")

mask = country == "Italy"
sales_italy = sales[mask]

distribution_plotter(sales_italy, "Ventas Italia")

mask = country == "France"
sales_france = sales[mask]

distribution_plotter(sales_france, "Ventas Francia")

sales = data_type_float[:,1]
distribution_plotter(sales, "Ventas Total")

"""## Ejercicio 3
Para los tres países del punto anterior, calcular con dos decimales
* Media
* Mediana
* Rango
* Desvío estandard

Repetir para todos los datos de ventas sin distinguir por país.

¿Qué conclusiones pueden sacar respecto a la información que brinda cada una de estas medidas en este caso particular?
"""

media_germany = round(np.mean(sales_germany),2)
mediana_germany = round(np.median(sales_germany),2)
max_germany = np.max(sales_germany)
min_germany = np.min(sales_germany)
rango_germany = round((max_germany - min_germany),2)
desvio_germany = round(np.std(sales_germany),2)

print(f"Media : {media_germany} \nMediana: {mediana_germany} \nRango: {rango_germany} \nDesvío Estandard: {desvio_germany}")

media_italy = round(np.mean(sales_italy),2)
mediana_italy = round(np.median(sales_italy),2)
max_italy = np.max(sales_italy)
min_italy = np.min(sales_italy)
rango_italy = round((max_italy - min_italy),2)
desvio_italy = round(np.std(sales_italy),2)

print(f"Media : {media_italy} \nMediana: {mediana_italy} \nRango: {rango_italy} \nDesvío Estandard: {desvio_italy}")



media_france = round(np.mean(sales_france),2)
mediana_france = round(np.median(sales_france),2)
max_france = np.max(sales_france)
min_france = np.min(sales_france)
rango_france = round((max_france - min_france),2)
desvio_france = round(np.std(sales_france),2)

print(f"Media : {media_france} \nMediana: {mediana_france} \nRango: {rango_france} \nDesvío Estandard: {desvio_france}")

media = round(np.mean(sales),2)
mediana = round(np.median(sales),2)
max = np.max(sales)
min = np.min(sales)
rango = round((max - min),2)
desvio = round(np.std(sales),2)

print(f"Media : {media} \nMediana: {mediana} \nRango: {rango} \nDesvío Estandard: {desvio}")
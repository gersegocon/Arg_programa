
"""Final_Analisis_de_datos_Etapa_1.ipynb

Tal y cómo lo hicimos durante el curso, dentro de la carpeta denominada como AP_UNdeC, y dentro de Data, podrás encontrar un archivo denominado winemag-data-130k-v2.csv, este archivo será el que usaremos para todo el desafío.
"""

import pandas as pd
import numpy as np

from google.colab import drive
drive.mount('/content/drive')
pathCurso = '/content/drive/MyDrive/AP_UNdeC/Data/'
ruta_archivo = pathCurso + 'winemag-data-130k-v2.csv'
wine_reviews_df = pd.read_csv(ruta_archivo)
del wine_reviews_df['Unnamed: 0']
wine_reviews_df.head(2)

"""**1)** *¿El campo designation, es el que más datos ausentes tiene, luego de region_2?*"""

display(wine_reviews_df.isna().sum())

"""**2)** *¿De los países que hay, Argentina tiene 3800 referencias, encontrándose en 6to lugar?*"""

mask_argentina = wine_reviews_df['country'] == 'Argentina'

print(wine_reviews_df[mask_argentina].shape[0])

print(wine_reviews_df['country'].value_counts())

mask1 = wine_reviews_df['country'] == 'Spain'
mask2 = wine_reviews_df['country'] == 'Italy'
mask3 = wine_reviews_df['country'] == 'France'

suma_italia_espa = wine_reviews_df[mask1]+wine_reviews_df[mask2]
print("Italia y España: ",suma_italia_espa.shape[0])
print("Francia: ", wine_reviews_df[mask3].shape[0])

"""**3)** *¿De las referencias de Argentina, hay 55 datos ausentes en el campo price?*"""

df_argentina = wine_reviews_df[mask_argentina]
display(df_argentina['price'].isna().sum())

"""**4)** *La mayor cantidad de referencias de vinos en Argentina son de la vinería "Trapiche"*"""

df_argentina['winery'].value_counts()

"""**5)** *La bodega mejor puntuada de Argentina es Bodega Catena Zapata*"""

mask_argentina = wine_reviews_df['country'] == 'Argentina'

df_argentina = wine_reviews_df[mask_argentina]
display(df_argentina['price'].isna().sum())

df_argentina[df_argentina["points"]==df_argentina["points"].max()]

"""**6)** *El vino más caro de Argentina es de la bodega Bodega Catena Zapata*"""

df_argentina[df_argentina["price"]==df_argentina["price"].max()]

"""**7)** *El vino más caro pertenece a la Bodega de Château les Ormes Sorbet*"""

wine_reviews_df[wine_reviews_df["price"]==wine_reviews_df["price"].max()]

"""**8)** *¿El precio más barato de vino es de 4 dólares, y hay un total cuantas referencias a vinos de ese precio?*"""

wine_reviews_df[wine_reviews_df["price"]==wine_reviews_df["price"].min()].shape[0]

"""**9)** *Índia es el país que tiene en promedio, el punto más bajo.*"""

# mask_india = wine_reviews_df['country'] == 'India'
# df_india = wine_reviews_df[mask_india]
# df_india['points'].mean()

group_by_pais = wine_reviews_df.groupby(['country'])
puntos_paises= group_by_pais.mean()
puntos_paises.sort_values('points')

puntos_paises.sort_values('price')

"""**10)** *¿Cuántas personas fueron las que testearon los vinos?*"""

wine_reviews_df['taster_name'].nunique()

"""**11)** *Teniendo en cuenta a las siguientes personas, marca de acuerdo a la cantidad de referencias que hicieron que lugar ocupa cada uno de ellos, considerando como primer puesto al que más referencias hizo.*"""

mask_n1 = wine_reviews_df['taster_name'] == 'Roger Voss'
mask_n2 = wine_reviews_df['taster_name'] == 'Kerin O’Keefe'
mask_n3 = wine_reviews_df['taster_name'] == 'Michael Schachner'

df_tester1 = wine_reviews_df[mask_n1]
df_tester2 = wine_reviews_df[mask_n2]
df_tester3 = wine_reviews_df[mask_n3]

print("Roger Voss: ",df_tester1.shape[0])
print("Kerin O’Keefe: ",df_tester2.shape[0])
print("Michael Schachner: ",df_tester3.shape[0])

"""**Manipulación de los datos**

*Asumiendo que en datos, tienes almacenado los datos del DataFrame original, sin alteraciones, ejecuta el siguiente comando, para generar una copia del DataFrame:*

`datos_copy = datos.copy(deep = True)`

Luego, elimina las columnas:

region_2

taster_twitter_handle

designation

(Asumiendo que Unnamed: 0 ya la habías eliminado)

Ahora por último, elimina todos los valores ausentes, considerando las filas.


"""

datos_copy = wine_reviews_df.copy(deep = True)

del datos_copy['region_2']
del datos_copy['taster_twitter_handle']
del datos_copy['designation']

"""**12)** *Luego de hacer la eliminación, ¿Cuántos países quedaron?*"""

datos_elim= datos_copy.dropna(axis=0)
datos_elim['country'].nunique()

"""**13)** *En promedio, Argentina tiene el precio más bajo, luego de eliminar los núlos*"""

group_by_pais2 = datos_elim.groupby(['country'])
puntos_paises2= group_by_pais2.mean()
puntos_paises2.sort_values('price')

"""**14)** *Luego de eliminar los nulos, de los países que quedaron,*  
`Seleccione una opción` *es el que menos referencias tiene y*  
`Seleccione una opción` *es el que más tiene*
"""

datos_elim['country'].value_counts()

"""**15)** *Luego de eliminar los nulos, en US, la tercer provincia que más referencias tiene es:*"""

mask_us = datos_elim['country'] == 'US'
us_prov = datos_elim[mask_us]
us_prov['province'].value_counts()

"""**16 y 17)** *Luego de eliminar, en Italy, la provincia que menos referencias tiene es Northwestern Italy, ¿con cuantas referencias?*

*Luego de haber eliminado los nulos, en Italy, específicamente en la provincia de Tuscany, ¿cuántas referencias se redujeron?*







"""

mask_italy_antes = wine_reviews_df['country'] == 'Italy'
italy_prov_antes = wine_reviews_df[mask_italy_antes]
mask_tuscany_antes = italy_prov_antes['province'] == 'Tuscany'
italy_tuscany_antes = italy_prov_antes[mask_tuscany_antes]
print("Antes de eliminar:")
print(italy_prov_antes['province'].value_counts())

mask_italy = datos_elim['country'] == 'Italy'
italy_prov = datos_elim[mask_italy]
mask_tuscany = italy_prov['province'] == 'Tuscany'
italy_tuscany = italy_prov[mask_tuscany]
print("\nDespues de eliminar:\n",italy_prov['province'].value_counts())

print("\nTUSCANY antes de eliminar: ")
print(italy_tuscany_antes.shape[0])
print("\nTUSCANY despues de eliminar: ")
print(italy_tuscany.shape[0])
print("\nSe redujo: ",italy_tuscany_antes.shape[0]-italy_tuscany.shape[0])

"""**18)** *Luego de haber eliminado los nulos ¿Cuáles son las 3 primeras bodegas de Argentina que producen una Variedad Syrah?*"""

mask_argentina_elim = datos_elim['country'] == 'Argentina'
datos_elim_argentina = datos_elim[mask_argentina_elim]
mask_variedad = datos_elim_argentina['variety'] == 'Syrah'
datos_elim_argentina_syrah = datos_elim_argentina[mask_variedad]
datos_elim_argentina_syrah['winery'].value_counts()

"""**19)** *Luego de haber eliminado los nulos, el vino con la descripción más larga corresponde a Domaine Ostertag 2015 Muenchberg*"""

datos_elim['largo_description'] = datos_elim['description'].apply(lambda x: len(x))
mask_larga = datos_elim['largo_description'] ==datos_elim['largo_description'].max()
dato99 = datos_elim[mask_larga]
dato99

del datos_elim['largo_description']

"""Ahora por último, completa:

Con el valor de la Mediana para el campo 'points'

Con el valor de la Media para el campo 'price'

"""

mediana = datos_elim['points'].median()
datos_elim['points'] = datos_elim['points'].fillna(mediana)

media = datos_elim['price'].mean()
datos_elim['price'] = datos_elim['price'].fillna(media)

"""**20)** *Luego de haber imputado los datos, el rango intercuartílico de points, para Argentina, es:*"""

mask_argentina_elim_2 = datos_elim['country'] == 'Argentina'
datos_elim_2 = datos_elim[mask_argentina_elim_2]
datos_elim_2.quantile([0.25,0.75])

"""**21)** *Selecciona el diagrama de caja, sobre los datos correspondientes a 'price' teniendo en cuenta a Spain, usando la configuración por
defecto de matp*
"""

import seaborn as sns
import matplotlib.pyplot as plt

mask_spain_elim = datos_elim['country'] == 'Spain'
datos_elim_spain = datos_elim[mask_spain_elim]
datos_elim_spain.quantile([0.25,0.75])

sns.boxplot(x=datos_elim_spain["price"])
plt.show()

"""**22)** *Selecciona el diagrama de caja, sobre los datos correspondientes a 'points' teniendo en cuenta a todas las provincias de Italy,
menos a Tuscany*
"""

mask_italy_elim = datos_elim['country'] == 'Italy'
datos_elim_italy = datos_elim[mask_italy_elim]
mask_sintuscany = datos_elim_italy['province'] == 'Tuscany'
sintuscany = datos_elim_italy.drop(datos_elim_italy[mask_sintuscany].index)

sintuscany.quantile([0.25,0.75])

sns.boxplot(x=sintuscany["points"])
plt.show()

"""**22)** *Realizando una agrupación de los datos, por el campo region_1 en Argentina, quien tiene el segundo valor más alto en media del precio es la Región de "Perdriel", ¿Cuánto es ese valor de media?*

Selecciona la opción más cercana
"""

grupo_by_region1 = datos_elim_2.groupby(['region_1'])
grupo_by_region1.mean().sort_values('price',ascending=False)

"""**23)** *Utilizando Seaborn con valores por  defecto.*

*Selecciona el gráfico de la distribución univariante del precio de todas las referencias relacionadas a Brazil, en el campo country*
"""

mask_brazil = wine_reviews_df['country'] == 'Brazil'
datos_brazil = wine_reviews_df[mask_brazil]

sns.distplot(datos_brazil['price'])
plt.show()

"""**24)** *Usando seaborn con valores por defecto, cual de las siguientes gráficas es la que corresponde a un Trazado de la distribución bivariante de los campos price en el eje x con points en el eje y de las referencias de Argentina*




"""

sns.jointplot(x="price", y="points", data=df_argentina)

plt.show()

"""**25)** *Selecciona el gráfico de bandas correspondiente para el taster_name en y,  contra points en x, usando valores por defecto, para todas las referencias de US*"""

sns.stripplot(y="taster_name", x="points", data=us_prov,legend=False, jitter=False)

plt.show()
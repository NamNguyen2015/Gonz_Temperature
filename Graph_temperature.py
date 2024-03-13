# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 14:09:17 2024

@author: marinas
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, HourLocator
import datetime as dt


# Nombre del archivo CSV
archivo_csv = "2024_03_11 CABR bridge temperature.csv"

# Importar el archivo CSV como DataFrame, omitiendo las primeras 5 filas
df = pd.read_csv(archivo_csv, skiprows=5, encoding='latin1')

# Rename the third column to "Temp"
df = df.rename(columns={df.columns[2]: 'Temp'})

# Combine the date and time columns into a single datetime column
df['DateTime'] = df[df.columns[0]] + ' ' + df[df.columns[1]]
df['DateTime'] = df['DateTime'].apply(lambda x: 
                 dt.datetime.strptime(x, '%B %d, %Y %I:%M:%S %p'))



# Calcular la media móvil 
nr_hours = 12  # Media móvil de tantas horas
rolling_mean = df['Temp'].rolling(window= nr_hours * 60).mean()
    

# Configurar el gráfico
plt.figure(figsize=(10, 6))  # Ajusta el tamaño del gráfico según tus preferencias

# Graficar los datos
plt.plot(df['DateTime'], df['Temp'], color='blue', marker='.', linestyle='-')

# Graficar la media móvil
plt.plot(df['DateTime'], rolling_mean, color='black', linestyle='--', linewidth=2)


# Personalizar los ejes
plt.xlabel('Date and Time', fontsize=14)  # Etiqueta del eje x
plt.ylabel('Temperature [°C]', fontsize=14)  # Etiqueta del eje y

# Configurar el formato de las fechas
date_format = DateFormatter('%m-%d\n%H:%M')  # Formato de fecha 'MM-DD HH:MM'
plt.gca().xaxis.set_major_formatter(date_format)

# Configurar los marcadores de las fechas
plt.gca().xaxis.set_major_locator(HourLocator(interval=6))  # Mostrar etiquetas cada 6 horas

# Rotar las etiquetas del eje x para una mejor legibilidad
plt.xticks(rotation='vertical')

# Añadir título al gráfico
plt.title('TEMPERATURE VARIATION', fontsize=16)

# Mostrar la cuadrícula
plt.grid(True)

# Añadir leyenda
plt.legend(['Temperature', f'{nr_hours}-hour Moving Average'], loc='upper left')

# Guardar el gráfico como PDF en tamaño A4 horizontal
plt.savefig('Temperature_plot.pdf', format='pdf', bbox_inches='tight')


# Mostrar el gráfico
plt.tight_layout()  # Ajustar el diseño para que todo quepa correctamente
plt.show()
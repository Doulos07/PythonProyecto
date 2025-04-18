import csv
import paths


ruta = paths.trimestres_hogar

def medir_densidad(personas, habitaciones) :
     densidad = round(personas / habitaciones)
     if densidad < 1 :
          return 'Bajo'
     elif 1 < densidad > 2 :
          return 'Medio'
     else :
          return 'Alto'

with ruta.open(encoding='utf-8') as archivo :
     read = csv.DictReader(archivo, delimiter=';')
     headers = read.fieldnames + ['DENSIDAD_HOGAR']
     data = list(read)

with ruta.open('w', newline='') as archivo :
     write = csv.DictWriter(archivo, headers, delimiter=';')
     write.writeheader()
     for filas in data :
         filas['DENSIDAD_HOGAR'] = medir_densidad(filas['TIPO_HOGAR'], filas['IX_TOT'])
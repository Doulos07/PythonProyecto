import csv
import paths

ruta = paths.trimestres_hogar

def tipo_hogar (tipo) :
     if 5 <= tipo >= 7 :
          return 'Material precario'
     elif tipo >= 4 :
          return 'Material durable'
     else :
          return 'No aplica' 

with ruta.open(encoding='utd-8') as archivo :
     read = csv.DictReader(archivo, delimiter=';')
     headers = read.fieldnames + ['MATERIAL_TECHUMBRE']
     data = list(read)

with ruta.open('w', newline='') as archivo :
     write = csv.DictWriter(archivo, headers, delimiter=';')
     write.writeheader()
     for filas in data :
         filas['MATERIA:_TECHUMBRE'] = tipo_hogar(filas['V4'])
         write.writerow(filas)
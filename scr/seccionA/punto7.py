import bootstrap
import csv
import paths

ruta = paths.trimestres_hogar

def tipo_hogar (cantidad) :
     cantidad = int(cantidad)
     if cantidad == 1 :
         return 'Unipersonal'
     elif 2 <= cantidad <= 4 :
         return 'Nuclear'
     else :
         return 'Extendido'

with ruta.open(encoding='utf-8') as archivo :
     read = csv.DictReader(archivo, delimiter=';')
     headers = read.fieldnames + ['TIPO_HOGAR']
     data = list(read)

with ruta.open('w', newline='', encoding = 'utf-8') as archivo :
     write = csv.DictWriter(archivo, headers, delimiter=';')
     write.writeheader()

     for filas in data :
         filas['TIPO_HOGAR'] = tipo_hogar(filas['IX_TOT'])
         write.writerow(filas)

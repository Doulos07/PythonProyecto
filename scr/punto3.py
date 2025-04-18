import paths
import csv

ruta = paths.trimestres_individual

with ruta.open() as archivo :
     read = csv.DictReader(archivo, delimiter=';')
     headers = read.fieldnames + ['CH04_str']
     filas = list(read)

with ruta.open('w', newline = '', encoding = 'utf-8') as archivo :
      write = csv.DictWriter(archivo,fieldnames= headers, delimiter= ';')
      write.writeheader()

      for fila in filas :
           fila['CH04_str'] = 'Masculino' if fila['CH04'] == '1' else 'Femenino' 
           write.writerow(fila)


         
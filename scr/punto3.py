import paths
import csv


with paths.trimestres_individual.open() as archivo :
     read = csv.DictReader(archivo, delimiter=';')
     headers = read.fieldnames + ['CH04_str']
     filas = list(read)

with paths.trimestres_individual.open('w', newline = '', encoding = 'utf-8') as archivo :
      write = csv.DictWriter(archivo,fieldnames= headers, delimiter= ';')
      write.writeheader()

      for fila in filas :
           fila['CH04_str'] = 'Masculino' if fila['CH04'] == '1' else 'Femenino' 
           write.writerow(fila)


         
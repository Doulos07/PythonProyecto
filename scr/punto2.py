import paths
import csv

hogar = []
#incluye Header
with paths.primer_hogar.open(encoding='utf-8') as archivo :
     read = csv.reader(archivo, delimiter=';')
     for filas in read :
         hogar.append(filas) 

#excluye header de 2do y 3er trimestre
with paths.segundo_hogar.open(encoding='utf-8') as archivo :
     read = csv.reader(archivo, delimiter=';')
     next(read)
     for filas in read :
         hogar.append(filas)

with paths.tercer_hogar.open(encoding='utf-8') as archivo :
     read = csv.reader(archivo, delimiter=';')
     next(read)
     for filas in read :
         hogar.append(filas)

with paths.trimestres_hogar.open('w', newline='') as archivo :
     write = csv.writer(archivo, delimiter=';')
     for filas in hogar :
          write.writerow(filas)



ind1 =csv.DictReader(open(paths.primer_individual),delimiter=";") 
ind2 =csv.DictReader(open(paths.segundo_individual),delimiter=";") 
ind3 =csv.DictReader(open(paths.tercer_individual),delimiter=";") 

#abrimos los archivos dataset donde vamos a poner los datos
dataSetIndividual = (open(paths.trimestres_individual,"w",newline="")) 

write_ind = csv.DictWriter(dataSetIndividual,fieldnames=ind1.fieldnames, delimiter=";")

write_ind.writeheader()

for line in ind1:
    write_ind.writerow(line)
for line in ind2:
    write_ind.writerow(line)
for line in ind3:
    write_ind.writerow(line)

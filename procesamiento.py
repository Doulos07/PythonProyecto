from pathlib import Path
import csv
from collections import Counter

#rutas de archivos
ruta_individual = Path ("datasets") / "3erTrimestre" / "usu_individual_T324.txt"
ruta_hogar = Path ("datasets") / "3erTrimestre" / "usu_hogar_T324.txt"

hombres = 0
mujeres = 0
propietarios = 0
propiedades = 0

dict_individuo = []
dict_hogar = []

pondera = set()
viviendas = set()

#--------------------------------------------------leer archivos
with ruta_individual.open (encoding="utf-8") as archivo :
      read = csv.DictReader(archivo, delimiter=";")
      for list in read :
           dict_individuo.append(list) #consumo el dict para hacer uno no consumible

          
with ruta_hogar.open (encoding='utf-8') as archivo :
      read = csv.DictReader(archivo, delimiter=';')
      for list in read :
           dict_hogar.append(list)
#--------------------------------------------------

#Hombres / Mujeres
for elem in dict_individuo :
     if(elem['CH04'] == '1') :
           hombres += 1
     else :
           mujeres += 1
 
#Mayores con Secundario
secundario_completo = 0
mayores = filter(lambda x : int(x['CH06']) >= 18, dict_individuo)

for elem in mayores :
     if int(elem['NIVEL_ED']) >= 4 :
           secundario_completo += 1

#cant_viviendas
for elem in dict_hogar :
      viviendas.add(elem['CODUSU'])
      propietarios += 1 if elem['II7'] == "1" else 0
      propiedades = len(viviendas)

#Aglomerado
filtro = filter(lambda x : x['IV8'] == '2' and x ['IX_TOT'] > '2', dict_hogar)

counter_aglomerado = Counter(int(x['AGLOMERADO']) for x in filtro)
mayor_aglomerado = counter_aglomerado.most_common(1) # devuelve el diccionario con solo un 1 elemento, el mayor
print(mayor_aglomerado)
menor_aglomerado = min(counter_aglomerado.items(), key= lambda x: x[1]) #de vuelve una tupla
print(f"mayor aglomerado es {mayor_aglomerado[0][0]} con un total de : {mayor_aglomerado[0][1]}")
print(f"menor aglomerado es {menor_aglomerado[0]} con un total de : {menor_aglomerado[1]}")

print(f"hombres:{hombres}\nmujeres:{mujeres}")
print(f"personas mayores con secundario completo : {secundario_completo}")
print(f"\n")
print(f"propietarios : {propietarios}")
print(f"propiedadeds : {propiedades}")
print(f"{int((propietarios/propiedades) *100)}%")


    

      
'''
IV8 N (1) ¿Tiene baño / letrina?
1 = Sí
2 = No

IX_TOT  N (2) Cantidad de miembros del hogar

'''
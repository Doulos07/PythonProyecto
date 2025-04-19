import boostrap
from paths import rutas
import manejoDeArchivo
archivo = manejoDeArchivo.crearRuta() 

path = ''
encontrado = False

for ruta in rutas :
     if archivo in ruta.name :
         encontrado = True
         path = ruta
         print(f"el archivo esta en la ruta : {ruta}")
         break

if encontrado :
      total = 0
      universitario = 0
      data = manejoDeArchivo.leerArchivo(path)
      for fila in data :
           if fila['CH15'] in ('4','5') :
                total += 1
                universitario += 1 if fila['CH12'] in ('7','8') else 0
      print(f'el porcentaje de personas no Argentinas con nivel Universitario o superior son : {round((universitario/total)*100, 2)}%')
else : 
      print('el archivo no se encontro') 

'''
     CH15 -> 4 or 5
     CH12 -> 7 or 8
'''
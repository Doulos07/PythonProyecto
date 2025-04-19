import csv

def leerArchivo(ruta) :
     with ruta.open(encoding = 'utf-8') as archivo :
          read = csv.DictReader(archivo, delimiter=';')
          return list(read)


def crearRuta () :
     ingresado = input("ingrese año y trimestre del archivo formato '2024 3' : ")

     archivo = ingresado.strip().split()
     archivo = f"usu_individual_T{archivo[1]}{archivo[0][2:]}.txt"   
     return archivo
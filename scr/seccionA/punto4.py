import bootstrap
import csv
import paths

ruta = paths.trimestres_individual
educacion = {
    "1": "Primario incompleto",
    "2": "Primario completo",
    "3": "Secundario incompleto",
    "4": "Secundario completo",
    "5": "Superior o universitario",
    "6": "Superior o universitario",
    "7": "Sin información",
    "9": "Sin información"
}

with ruta.open(encoding='utf-8') as dataSetIndividual :
    data = csv.DictReader(dataSetIndividual,delimiter=";")
    datos = list(data)
    titulo_nuevo = data.fieldnames + ['NIVEL_ED_str']

with ruta.open('w', newline='', encoding = 'utf-8') as dataSetIndividual:
    data = csv.DictWriter(dataSetIndividual,fieldnames=titulo_nuevo,delimiter=";")
    data.writeheader()
    for fila in datos:
        fila['NIVEL_ED_str'] = educacion[fila['NIVEL_ED']]
        data.writerow(fila)
import csv
import paths

condicion = {
    "1" : ["Ocupado autonomo", "Ocupado dependiente"],
    "2" : "Desocupado",
    "3" : "inactivo",
    "4" :  "Fuera de categoría/sin información"
}

with paths.trimestres_individual.open() as dataSetIndividual:
    data = csv.DictReader(dataSetIndividual,delimiter=";")
    datos= list(data)
    titulo_nuevo = data.fieldnames + ["CONDICION_LABORAL"]

with paths.trimestres_individual.open ("w", newline='') as dataSetIndividual:
     data = csv.DictWriter(dataSetIndividual,fieldnames=titulo_nuevo,delimiter=";")
     data.writeheader()
     for line in datos:
         if (line["ESTADO"] == "1") :
             line["CONDICION_LABORAL"] = condicion["1"][0] if line["CAT_OCUP"] in ("1", "2") else condicion["1"][1]
         elif(line["ESTADO"] != "0") :
             line["CONDICION_LABORAL"] = condicion[line["ESTADO"]]
         data.writerow(line)
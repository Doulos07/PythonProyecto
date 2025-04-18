import csv
import paths

ruta = paths.trimestres_individual

with ruta.open (encoding = 'utf-8') as dataSetIndividual:
    data = csv.DictReader(dataSetIndividual,delimiter=";")
    datos = list(data)
    titulo_nuevo = data.fieldnames + ["UNIVERSITARIO"]

with ruta.open ("w", newline='', encoding = 'utf-8') as dataSetIndividual:
    data = csv.DictWriter(dataSetIndividual,fieldnames=titulo_nuevo,delimiter=";")
    data.writeheader()
    for line in datos:
        
        año=int(line["CH05"][6:]) # 26/12/2014 Tomo del 6to indice al ultimo = 2014
        edad = 2025 - año
        if(edad < 18):
            line["UNIVERSITARIO"] = "2"
        else:
            if(line["NIVEL_ED"] == "6"):
                line["UNIVERSITARIO"]= "1"
            else:
                line["UNIVERSITARIO"]="0"
        data.writerow(line)


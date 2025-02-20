import csv

with open("csvEjem.csv", "r", newline="", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    
    for fila in lector:
        print(fila)

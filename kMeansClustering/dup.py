import csv

# kleines Python-Programm, das die Zeilen ausgibt, in der Duplikate im Datensatzes vorhanden sind (dient der Verifizierung)

dups = []
index_bin = []

with open('./iris.csv') as data:
    lines = data.readlines()
    for actLine in range(0,148):
        for compLine in range(1,149):
            if lines[actLine] == lines[compLine] and actLine != compLine:
                dups.append([actLine, compLine])
    for dup in dups:
        if dup[0] < dup[1]:
            temp = dup[0]
            dup[0] = dup[1]
            dup[1] = temp
    print("DUPS:", dups)
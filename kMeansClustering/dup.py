import csv

with open('iris.csv') as data:
    lines = data.readlines()
    for actLine in range(0,148):
        for compLine in range(1,149):
            if lines[actLine] == lines[compLine] and actLine != compLine:
                print(actLine, compLine)
                print(lines[actLine], lines[compLine])
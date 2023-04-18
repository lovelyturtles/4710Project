from efficient_apriori import apriori
import csv
import pandas as pd

with open('in.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    output = list(reader)


transaction = [tuple(elem) for elem in output]

minsup = float(input("Minimum Support: "))
minconf = float(input("Minimum Confidence: "))

itemsets, rules = apriori(transaction, min_support=minsup, min_confidence=minconf)

f = open("apriori_out.txt","w")

for r in rules:
    f.write(str(r) + "\n")
    
f.close()

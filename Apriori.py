from efficient_apriori import apriori
import csv
import pandas as pd



with open('apriori_cleaned_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    output = list(reader)


transaction = [tuple(elem) for elem in output]

itemsets, rules = apriori(transaction, min_support=0.001, min_confidence=0.003)

f = open("out_priori.txt","w")

for r in rules:
    f.write(str(r) + "\n")
    
f.close()

print(rules)

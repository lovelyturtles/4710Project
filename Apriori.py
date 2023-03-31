from efficient_apriori import apriori
import csv

with open('dataCleaned.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    output = list(reader)

[tuple(elem) for elem in output]

itemsets, rules = apriori(output, min_support=0.1, min_confidence=0.30)
print(rules)


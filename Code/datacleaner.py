import pandas
import time


start = time.time()

file = pandas.read_csv("../Data/data.csv",low_memory=False)

file.drop(file[file['Location'].isnull()].index, inplace = True)
file.drop(file[file['Location']== "(0.0, 0.0)"].index, inplace = True)
file = file.drop("Point",axis=1)

file['Date'] = pandas.to_datetime(file['Issue Date']).dt.date
file['Time'] = pandas.to_datetime(file['Issue Date']).dt.time

file = file.drop("Issue Date",axis=1)

print(file.dtypes)

file = file[['Date', 'Time', 'Violation', 'Street', 'Location',"Full Fine","Discounted Fine"]]

file.to_csv("../Data/out.csv",index=False)

end = time.time()

print(end-start)
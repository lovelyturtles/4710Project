# COMP 4170 Group 4: Analysis of Parking Violations in Winnipeg 

This project was for University of Manitoba's COMP 4710 Data Mining course taught by Dr. Carson K. Leung in Winter 2023.

This project was conducted by the following University of Manitoba students:
- Adrien Dinzey
- Agape Seo
- John Baptista
- Susie Kihaile

# Abstract

In many places, the number of parking violations are growing as the population and usage of vehicles increase. These illegal parking can lead to several problems such as increased congestion, decreases safety, and it makes the cities less clean and attractive. One city that is growing is the City of Winnipeg located in Manitoba, Canada. This paper focuses on the parking violations in the City of Winnipeg and attempts to determine what factors may lead to the number of parking violations it currently has.

# Organization

The repository is split into 3 folders. 
- 'Code' which contains all the code used in this project (all written in python)
- 'Data' contains the data used to run the code. The data.rar is the raw data from the City of Winnipeg Open Data Portal
- 'Results' contains the results from the algorithms we ran

# Installation

To run the code in the repository, you must install the following libraries:
- Python 3
- jupyter_notebook
- chart_studio
- cufflinks
- numpy
- pandas
- efficient_apriori
- matplotlib
- seaborn
- scikit-learn
- kmodes

# Execution
All the code to run the following is found in the 'Code' folder

## To run Preprocessing
1. Manually extract the 'data.rar' file in the 'Data' folder to a 'data.csv' file in the 'Data' folder
2. Open the 'preprocessor.ipynb' and run all
3. Open the 'exploration.ipynb' and run all
4. Open the 'mergeCodes.ipynb' and run all

## To run the data sampler for the algorithms
1. After the preprocessing steps above have ran, open the 'dataSampler.ipynb' file and run all. This produces a sample of about 100,000 rows to run the algorithms on.


Note: All of the following should be run after the preprocessing steps and the data sampler step above is completed. 
## To run the Data Visualization
1. Open the 'DataVisualization.ipynb' and run all
2. The results can be found in the jupyter notebook


## To run the Correlation Analysis
1. Open the 'correlationAnalysis.ipynb' and run all
2. The results can be found in the jupyter notebook


## To run the Apriori Algorithm
1. Open the 'apriori.ipynb' and 'aprioriwithMidnight.ipynb' and run all for both
2. The results can be found in the 'Results' folder:
- 'apriori_results.txt' for the 'apriori.ipynb' results
- 'apriori_with_midnight_results.txt' for the 'aprioriwithMidnight.ipynb' results


## To run the KModes Algorithm
1. Open the 'kModes.ipynb' and 'kModeswithMidnight.ipynb' and run all for both
2. The results can be found in the 'Results' folder:
- 'K-Modes_Cluster_Info.csv' for the 'kModes.ipynb' results
- 'K-Modes_Cluster_Info2.csv' for the 'kModes.ipynb' results
- 'K-Modes_Cluster_Info_midnight.csv' for the 'kModeswithMidnight.ipynb' results
- 'K-Modes_Cluster_Info_midnight2.csv' for the 'kModeswithMidnight.ipynb' results


## To run the DB Scan
1. Open the 'dbscan.ipynb' and 'dbscanwithMidnight.ipynb' and run all for both
2. The results can be found in the jupyter notebook


## To run the Decision Tree
1. Open the 'decisionTree.ipynb' and run all
2. The results can be found in the 'Results' folder as 'DT and RF results info.csv'


## To run the Random Forest
TO DO
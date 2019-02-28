import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

trainingData = pd.read_csv('raw_data/train.csv')
#We don't need the names of the animals
trainingData = trainingData.drop(['Name'],axis=1)
trainingData.columns = ['animal_ID','datetime','outcome','outcome_subtype','animal_species','gender','age_upon_exit','breed','color']
print(trainingData.head(10))
print('Outcome: ',trainingData['outcome'].unique())
print('Outcome_Subtype: ',trainingData['outcome_subtype'].unique())
print('Animal_Species: ',trainingData['animal_species'].unique())
print('Gender: ',trainingData['gender'].unique())
print('Breed: ',trainingData['breed'].unique())
print('Color: ',trainingData['color'].unique())

#n, bins, patches = plt.hist(x=trainingData['gender'], bins='auto',color = '#FF0000',alpha=.7,rwidth=.85)

trainingData['gender'].value_counts().plot(kind='bar')

#trainingData['gender'].plot.hist(grid=True,bins =trainingData['gender'].unique().size, rwidth = .9, color = '#FF0000')
plt.title('Gender')
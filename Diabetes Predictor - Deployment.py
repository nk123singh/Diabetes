# Importing essential libraries
import numpy as np
import pandas as pd
import pickle

# find the dataset in the repo store it in your project folder
# Loading the dataset
df = pd.read_csv('kaggle_diabetes.csv')

# Renaming DiabetesPedigreeFunction as DPF
df = df.rename(columns={'DiabetesPedigreeFunction':'DPF'})

# Replacing the 0 values from ['Glucose','BloodPressure','SkinThickness','Insulin','BMI'] by NaN
df_copy = df.copy(deep=True)
df_copy[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = df_copy[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.nan)

# Replacing NaN value by mean, median depending upon distribution
df_copy.fillna({'Glucose':df_copy['Glucose'].mean()}, inplace=True)
df_copy.fillna({'BloodPressure':df_copy['BloodPressure'].mean()}, inplace=True)
df_copy.fillna({'SkinThickness':df_copy['SkinThickness'].median()}, inplace=True)
df_copy.fillna({'Insulin':df_copy['Insulin'].median()}, inplace=True)
df_copy.fillna({'BMI':df_copy['BMI'].median()}, inplace=True)
# Model Building
from sklearn.model_selection import train_test_split
X = df.drop(columns='Outcome')
y = df['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

# Creating Random Forest Model
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=20)
classifier.fit(X_train, y_train)

# Creating a pickle file for the classifier
filename = 'diabetes-prediction-rfc-model.pkl'
pickle.dump(classifier, open(filename, 'wb'))

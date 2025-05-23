# -*- coding: utf-8 -*-
"""BaldnessModel.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aiAEaupiQzduDAFA13vtdlwTEMXuNNIv

My first machine learning model
"""

from google.colab import files
uploaded = files.upload()

import io
import pandas as pd
data_baldness = pd.read_csv(io.BytesIO(uploaded['Luke_hair_loss_documentation (2).csv']))

data_baldness["shampoo_brand"]

data_baldness.info()

data_baldness.describe()

data_baldness.hist()

data_baldness

data_baldness = data_baldness.drop(columns=['date '])

data_baldness

data_baldness.isna().sum()

"""We re going to fill every null atribute as a 0"""

data_baldness['dandruff'] = data_baldness['dandruff'].fillna(0)
data_baldness['hair_grease'] = data_baldness['hair_grease'].fillna(0)
data_baldness
data_baldness.isna().sum()

"""If we want to delete avery null attribute we should execute the following command"""

#data_baldness = data_baldness.dropna(how='any)
#data_baldness

"""Now we want to traduce the non numeric values to numeric values"""

data_baldness['hair_washing'].unique()

hair_washing_values = {"hair_washing": {"Y":1, "N":0 }}
data_baldness.replace(hair_washing_values, inplace=True)
data_baldness['hair_washing'].unique()

data_baldness['pressure_level'].unique()

pressure_level_values = {"pressure_level": {"Low":1, "Medium":2, "High":3, "Very High":4 }}
data_baldness.replace(pressure_level_values, inplace=True)
data_baldness['pressure_level'].unique()

data_baldness['stress_level'].unique()

stress_level_values = {"stress_level": {"Low":1, "Medium":2, "High":3, "Very High":4 }}
data_baldness.replace(stress_level_values, inplace=True)
data_baldness['stress_level'].unique()

data_baldness['shampoo_brand'].unique()

shampoo_brand_values = {"shampoo_brand": {"Pantene":1, "Hair & Shoulder":2}}
data_baldness.replace(shampoo_brand_values, inplace=True)
data_baldness['shampoo_brand'].unique()

data_baldness['swimming'].unique()

data_baldness_values = {"swimming": {"Yes":1, "No":0 }}
data_baldness.replace(data_baldness_values, inplace=True)
data_baldness['swimming'].unique()

hair_loss_values = {"hair_loss": {"Few":1, "Medium":2, "Many":3, "A lot":4 }}
data_baldness.replace(hair_loss_values, inplace=True)
data_baldness['hair_loss'].unique()

data_baldness["dandruff"].unique()

dandruff_values = {"dandruff": {"Few":1, "Many":2 }}
data_baldness.replace(dandruff_values, inplace=True)
data_baldness['dandruff'].unique()

data_baldness.info()

"""We are going to primt the related values to hair loss"""

import matplotlib.pyplot as plt
plt.scatter( x = data_baldness['pressure_level'], y = data_baldness['hair_loss'])
plt.title('Hair Loss vs Pressure Level')
plt.xlabel('Pressure Level')
plt.ylabel('Hair Loss')
plt.show()

plt.scatter( x = data_baldness['hair_washing'], y = data_baldness['hair_loss'])
plt.title(' Hair Washing vs Hair Loss')
plt.xlabel('Hair Washing')
plt.ylabel('Hair Loss')
plt.show()

plt.scatter( x = data_baldness['stress_level'], y = data_baldness['hair_loss'])
plt.title(' Stress Level vs Hair Loss')
plt.xlabel('Stress Level')
plt.ylabel('Hair Loss')
plt.show()



plt.scatter( x = data_baldness['hair_grease'], y = data_baldness['hair_loss'])
plt.title(' Hair Grease vs Hair Loss')
plt.xlabel('Hair Grease')
plt.ylabel('Hair Loss')
plt.show()

"""This dataset needs more values in order to create a better histogram to use good data, because we don't have any linnear regression and we need a tendency in order to  train the model.

**TRAINING THE MODEL**
"""

data_baldness

training_data = data_baldness.sample(frac=0.8, random_state=0)
test_data = data_baldness.drop(training_data.index)

training_data

"""Divide the prediction value and the training data"""

training_labels = training_data.pop('hair_loss')
test_labels = test_data.pop('hair_loss')

training_labels

training_data

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(training_data, training_labels)

predictions = model.predict(test_data)
predictions

import numpy as np
from sklearn.metrics import mean_squared_error
error = np.sqrt(mean_squared_error(test_labels, predictions))
print("Perceptual error: %f" % (error * 100))

"""The performance of the generated model is not satisfactory, as it shows an error rate of approximately 46%. This implies that if we use this model to predict whether someone will go bald, there's a high likelihood that the prediction will be incorrect. Therefore, this model is not a reliable or accurate option for making such predictions

**TEST of someone new trying our model**
"""

new_person = pd.DataFrame(
    np.array([[1,1,1,1,1,1,1,1,1.0,1,1]]), columns=['stay_up_late', 'pressure_level', 'coffee_consumed','brain_working_duration','stress_level','shampoo_brand','swimming','hair_washing','hair_grease','dandruff','libido'])
new_person

model.predict(new_person)

"""The issue has been identified: we either need to classify more data or use a different dataset, since our current model does not perform as well as expected.
Based on the prediction, the person we created is not likely to experience significant hair loss.
"""
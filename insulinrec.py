# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lxppuTfE1yOj_ncCNSJuvsKxnZ-WFppx
"""

import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the diabetes dataset
diabetes_df = pd.read_csv("insuline dose.csv")

# Select the predictor variables and the response variable
X = diabetes_df[['Weight (Kg)', 'Insulin sensitivity Factor', 'Current BG level', 'Target BG level', 'Basal (40-50%) units', 'Insulin to carbohydrate Ratio', 'CHO insulin dose', 'High blood sugar correction dose', 'Total CHO in a meal', 'Total Daily insulin requirement']]
y = diabetes_df['Total meal insulin dose']

# Split the data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Fit a linear regression model to the training data
model = LinearRegression()
model.fit(X_train, y_train)

# Print the coefficients of the model
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

# Evaluate the model on the test data
from sklearn.metrics import r2_score
y_pred = model.predict(X_test)
print("R-squared:", r2_score(y_test, y_pred))

# Ask the user to input values for a new data point
#should extract the user account details for weight and target

weight = float(input("Enter weight (in Kg): "))
total_cho = float(input("Enter total CHO in a meal: "))
current_bg = float(input("Enter current BG level: "))
target_bg = float(input("Enter target BG level: "))

# Calculate the "Total Daily insulin requirement" using a formula
total_daily_insulin = 0.55 * weight

# Calculate "Insulin sensitivity Factor" using the 1888 rule
insulin_sensitivity_factor = 1800 / total_daily_insulin

# Calculate "Insulin to carbohydrate Ratio" using the 500 rule
insulin_carb_ratio = 500 / total_daily_insulin

# Calculate "CHO insulin dose" by dividing "Total CHO in a meal" by "Insulin to carbohydrate Ratio"
cho_insulin_dose = total_cho / insulin_carb_ratio

# Calculate "High blood sugar correction dose" using the formula you provided
high_bg_correction_dose = (current_bg - target_bg) / insulin_sensitivity_factor

# Calculate "Basal (40-50%) units" using the formula you provided
basal_units = total_daily_insulin * (50 / 100)

# Print the calculated values
#print("Total Daily insulin requirement:", total_daily_insulin)
#print("Basal (40-50%) units:", basal_units)
#print("CHO insulin dose:", cho_insulin_dose)
#print("High blood sugar correction dose:", high_bg_correction_dose)


# Create a dictionary for the new data point with the calculated features
new_data = {'Weight (Kg)': weight, 
            'Insulin sensitivity Factor': insulin_sensitivity_factor, 
            'Current BG level': current_bg, 
            'Target BG level': target_bg, 
            'Basal (40-50%) units': basal_units, 
            'Insulin to carbohydrate Ratio': insulin_carb_ratio, 
            'CHO insulin dose': cho_insulin_dose, 
            'High blood sugar correction dose': high_bg_correction_dose, 
            'Total CHO in a meal': total_cho, 
            'Total Daily insulin requirement': total_daily_insulin}
# Make prediction for new data point
X_new = pd.DataFrame([new_data])
y_new = model.predict(X_new)

# Print the predicted total meal insulin dose
print("Predicted total meal insulin dose: {:.2f}".format(y_new[0]))

# Ask the user if they want to print additional features
print_additional_features = input("Do you want to print additional features? (yes or no): ")
if print_additional_features.lower() == 'yes':
 print("Total Daily insulin requirement: {:.2f}".format(total_daily_insulin))
 print("Basal (40-50%) units: {:.2f}".format(basal_units))
 print("CHO insulin dose: {:.2f}".format(cho_insulin_dose))
 print("High blood sugar correction dose: {:.2f}".format(high_bg_correction_dose))





#if print_additional_features.lower() == 'yes':
 #print("Total Daily insulin requirement:", total_daily_insulin)
 #print("Basal (40-50%) units:", basal_units)
 #print("CHO insulin dose:", cho_insulin_dose)
 #print("High blood sugar correction dose:", high_bg_correction_dose)
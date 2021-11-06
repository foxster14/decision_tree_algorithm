 # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics # Import scikit-learn metrics module for accuracy calculation
import xlsxwriter # Used to export data to Excel file
import matplotlib as plt # Used to create visual representation of graphs and data structures
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

## look at how to keep the nodes uniform

path = '/Users/sarahfox/OneDrive - Dunwoody College of Technology/Junior Year/Data Science/Decision Trees/' #path where all files are stored

filename = 'drug_classification.csv'

## Import sheets
data_frame = pd.read_csv(path + filename)

# Using Sex, Blood Pressure, and Cholesterol data to predict which drug
# the patient will need
x = data_frame[["Sex","BP","Cholesterol"]] # Features
y = data_frame["Drug"] # Target variable

titles = ["Sex","BP","Cholesterol","Drug"]

# "leaves" (aka decision nodes) are where we get final output
# root node is where the decision tree starts
# Create Decision Tree classifer object
decision_tree = DecisionTreeClassifier(criterion="entropy", max_depth=3)
one_hot_data = pd.get_dummies(x,drop_first=True)

# Train Decision Tree Classifer
decision_tree = decision_tree.fit(one_hot_data, y)

text_representation = tree.export_text(decision_tree, feature_names=titles)
print(text_representation)


# Predict the response for test dataset
##y_pred = decision_tree.predict(one_hot_data)


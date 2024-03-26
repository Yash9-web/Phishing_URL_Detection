# -*- coding: utf-8 -*-
"""lastfinal.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hz5f-neFLb7mB0DcMu66X4cZrM-TICsk
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Loading the data
df= pd.read_csv('5.urldata.csv')
df.head()

df['Label'].value_counts()

df.isnull().sum()

import matplotlib.pyplot as plt
!pip install plotly_express
import plotly_express as px
fig = px.histogram(df, x="Label", color="Label", color_discrete_sequence=["#871fff","#ffa78c"])
fig.show()

M=df['Domain']
len(M)
'''no of urls in dataset'''

y = df['Label']
X = df.drop(['Label', 'Domain'], axis=1)

# Splitting the dataset into train and test sets: 80-20 split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12)

Train=len(X_train)
test=len(X_test)
print(Train,test)

numeric_features = X.select_dtypes(include=['int64', 'float64']).columns
categorical_features = X.select_dtypes(include=['object']).columns

numeric_transformer = Pipeline(steps=[('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

model = DecisionTreeClassifier(max_depth=5)

pipe = Pipeline(steps=[('preprocessor', preprocessor), ('classifier', model)])

# Fitting the model with training data
pipe.fit(X_train, y_train)

# Predicting the target value for test data
y_test_pred = pipe.predict(X_test)
print(y_test_pred)

# Computing the accuracy of the model performance
acc_test = accuracy_score(y_test, y_test_pred)
print("Decision Tree: Accuracy on Test Data: {:.3f}".format(acc_test))
'''the error margin is 20%, the actual value for the data for testing is y_test and y_test__pred is prediction after training'''

df1= pd.read_csv('/content/testcase.csv')
n=int(input('enter the no of url from test dataset (row no)'))
n=n-1
n_url=df1['Domain'].iloc[n]
new_url_data = pd.DataFrame({'Have_IP': [df1['Have_IP'].iloc[n]],
    'Have_At': [df1['Have_At'].iloc[n]],
    'URL_Length': [df1['URL_Length'].iloc[n]],
    'URL_Depth': [df1['URL_Depth'].iloc[n]],
    'Redirection': [df1['Redirection'].iloc[n]],
    'https_Domain': [df1['https_Domain'].iloc[n]],
    'TinyURL': [df1['TinyURL'].iloc[n]],
    'Prefix/Suffix': [df1['Prefix/Suffix'].iloc[n]],
    'DNS_Record': [df1['DNS_Record'].iloc[n]],
    'Web_Traffic': [df1['Web_Traffic'].iloc[n]],
    'Domain_Age': [df1['Domain_Age'].iloc[n]],
    'Domain_End': [df1['Domain_End'].iloc[n]],
    'iFrame': [df1['iFrame'].iloc[n]],
    'Mouse_Over': [df1['Mouse_Over'].iloc[n]],
    'Right_Click': [df1['Right_Click'].iloc[n]],
    'Web_Forwards': [df1['Web_Forwards'].iloc[n]]
})
# Rest of your code
result = pipe.predict(new_url_data)
if (result==1):
    print(n_url,":is a phishing url")
else:
    print(n_url,":is a legitimate url")

fig1 = px.histogram(df1, x="Labels", color="Labels", color_discrete_sequence=["#871fff","#ffa78c"])
fig1.show()

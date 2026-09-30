import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('dectree.csv')
df = data.copy()
le = LabelEncoder()
df['Nationality']= le.fit_transform(df['Nationality'])
df['Go']=le.fit_transform(df['Go'])

x = df.drop('Go',axis=1)
y = df['Go']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

logreg = LogisticRegression(random_state=16)
logreg.fit(x_train, y_train)

from nicegui import ui

def root():
    with ui.card():
        with ui.grid(columns=2):
            with ui.grid(columns=2):
                ui.label("Age")
                age = ui.input(value='43')
            
                ui.label("Experience")
                exp = ui.input(value='0')
            
                ui.label("Rank")
                rank = ui.input(value='43')
    

def reverse(text: str) -> str:
    return text[::-1]

ui.run(root)






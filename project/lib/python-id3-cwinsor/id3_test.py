
import numpy as np 
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from id3 import ID3

data = pd.DataFrame(np.array([
    ["Sunny",    "Hot",  "High",   "Weak",   "No" ],
    ["Sunny",    "Hot",  "High",   "Strong", "No" ],
    ["Overcast", "Hot",  "High",   "Weak",   "Yes"],
    ["Rain",     "Mild", "High",   "Weak",   "Yes"],
    ["Rain",     "Cool", "Normal", "Weak",   "Yes"],
    ["Rain",     "Cool", "Normal", "Strong", "No" ],
    ["Overcast", "Cool", "Normal", "Strong", "Yes"],
    ["Sunny",    "Mild", "High",   "Weak",   "No" ],
    ["Sunny",    "Cool", "Normal", "Weak",   "Yes"],
    ["Rain",     "Mild", "Normal", "Weak",   "Yes"],
    ["Sunny",    "Mild", "Normal", "Strong", "Yes"],
    ["Overcast", "Mild", "High",   "Strong", "Yes"],
    ["Overcast", "Hot",  "Normal", "Weak",   "Yes"],
    ["Rain",     "Mild", "High",   "Strong", "No" ]]),
             columns=['Outlook', 'Temperature', 'Humidity', 'Wind', 'PlayTennis'])

attributes = ['Humidity', 'Wind', 'Outlook']
target_attribute = "PlayTennis"

id3_instance = ID3()
id3_instance.fit(data, target_attribute, attributes)

print("xxxxxxxxxxxxxxxxxxxxxxxxx")
id3_instance.traverse("")

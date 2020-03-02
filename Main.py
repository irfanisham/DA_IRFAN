import numpy as np
import pandas as pd

names = ['Japan', 'Taiwan', 'Hong Kong']
years = ['2010', '2012', '2014']
month = ['Jan', 'Feb', 'Mar']

dict = {"country": ["Japan", "Taiwan", "Hongkong"],
        "years": ["2010", "2012", "2014"],
        "month" : ["Jan", "Feb", "Mar"]}
brics = pd.dataframe(dict)
print(brics)




class calutils :
    country = []
    year = []
    month = []

    class DA :
        def read_data(self):
            file = "Worksheet in Lesson 2019 Applied Scripting using Python Pyhton Elective (IT49450) - Project_14Mar19.csv"
            df = pd.read_csv(file)


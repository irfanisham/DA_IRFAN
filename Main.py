import numpy as np
import matplotlib as plt
import pandas as pd

class DA:
        def read_data(self):
            file = "Worksheet in D  Lesson 2019 Applied Sripting Using Python Python Elective (IT49450) - Project_14Mar19.csv"
            df = pd.read_csv(file)
            print(df)



            print(df.iloc[1:129, 0:19])




country = DA()
country.read_data()


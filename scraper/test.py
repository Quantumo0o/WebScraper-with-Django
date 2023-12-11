import os
import pandas as pd

def duplicate(filename):
    print("1")
    data = pd.read_csv(filename)
    data.drop_duplicates(inplace=True)
    print(data)
    data.to_csv(filename, index=False)


filename= os.path.join("csv","iphone.csv")
duplicate(filename)


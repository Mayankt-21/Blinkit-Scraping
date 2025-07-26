import numpy as np
import pandas as pd

def loadData():
    categories_list = np.genfromtxt("./datasets/blinkit_categories.csv", delimiter="," , dtype="str",skip_header=1)
    location_list = np.genfromtxt("./datasets/blinkit_locations.csv" , delimiter=",",dtype="str",skip_header=1)
    
    return categories_list,location_list
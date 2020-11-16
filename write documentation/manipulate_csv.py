# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
from pathlib import Path
LOC = Path(r"C:\Users\massetti\OneDrive - Sierentz & CIE\Documents\Python Scripts\testRoman")


def create_dummy_csv(random_seed=3):
    """
    @Roman could you please write the right documentation for this function?

    """
    the_csv = pd.DataFrame(columns=["test1", "test2"])
    the_csv["test1"] = np.random.rand(10, seed=random_seed)# not sure if the seed is a correct input to np.random.rand, could you check it for me please?
    the_csv["test2"] = np.random.rand(10, seed=random_seed)
    the_csv.to_csv(str(LOC / "write documentation" / "the_csv.csv"), index=False)
    print("saved the csv at {}".format(LOC))#TODO! should I have LOC as an argument?
    return True

def read_the_csv(name_of_the_csv):
    the_csv = pd.read_csv(name_of_the_csv)
    return the_csv

#    the_csv.plot()

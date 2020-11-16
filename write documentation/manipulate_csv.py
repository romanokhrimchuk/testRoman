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
    the_csv = pd.DataFrame(columns=["test1", "test2"])
    the_csv["test1"] = np.random.rand(10, seed=random_seed)
    the_csv["test2"] = np.random.rand(10, seed=random_seed)
    the_csv.to_csv(str(LOC / "write documentation" / "the_csv.csv"), index=False)
    print("saved the csv at {}".format(LOC))#TODO! should I have LOC as an argument?
    return True
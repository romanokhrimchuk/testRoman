# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import os

def create_dummy_csv(outname_csv='the_csv', output_path=None, 
                     random_seed=None, columns=["test1", "test2"], 
                     num_column_elements=10):
    """  
    The function creates .csv with randomly generated dummy data
    
    Parameters
    ----------
    outname_csv : str, default 'the_csv'
        The name with which the file will be save
    output_path : str, default None
        The path where the .csv file will be save. Current working 
        directory will be take as the path, if this parameter is not fill
    random_seed : int or 1-d array_like, default None
        Value of this parameter to use for initialization the random number 
        generator. The random number generator will start with it value, to
        be able to generate a random number. By default the random number 
        generator uses the current system time.
        Note: The parameter random_seed must be convertible to 32 bit unsigned 
        integers
    columns : list, default ["test1", "test2"]
        The name of columns which will be create
    num_column_elements : int, default 10
        Generates a given number of random values using the uniform 
        distribution over [0, 1) for every column
    """
    np.random.seed(random_seed)
    the_csv = pd.DataFrame(columns = columns, data = np.random.rand(num_column_elements,len(columns)))
    
    csv_save_path = output_path or os.getcwd()
    csv_save_path = os.path.join(csv_save_path,outname_csv+'.csv')
    the_csv.to_csv((csv_save_path), index=False)
    print("saved the csv at {}".format(csv_save_path))
    
    return True

def read_the_csv(name_of_the_csv):
    the_csv = pd.read_csv(name_of_the_csv)
    return the_csv

def plot_the_csv(the_csv):

    the_csv.plot()
#    how to save the figure in the format "yyyy_mm_dd-todays_csv.png"?
#    also including a legend, a4 page size and proper labels in the sides of the axes?

if __name__ == "__main__":
    output_path = r"C:\GitHub\exam\testRoman"
    name_of_the_csv = r"C:\GitHub\exam\testRoman\the_csv.csv"
    create_dummy_csv(outname_csv='the_csv', output_path=output_path, 
                     random_seed=None, columns=["test1", "test2"], 
                     num_column_elements=30)
    
    the_csv = read_the_csv(name_of_the_csv)
    plot_the_csv(the_csv)
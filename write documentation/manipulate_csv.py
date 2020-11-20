# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from datetime import datetime

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

def read_the_csv(path_to_csv):
    """
    Read a comma-separated values (csv) file into DataFrame
    
    Parameters
    ----------
    path_to_csv : str, path object or file-like object
        Any valid string path is acceptable. The string could be a URL. 
        Valid URL schemes include http, ftp, s3, gs, and file. For 
        file URLs, a host is expected. A local file could 
        be: file://localhost/path/to/table.csv.
        
    Returns 
    ------- 
    the_csv : DataFrame or TextParser
        A comma-separated values (csv) file is returned as
        two-dimensional data structure with labeled axes.
    """
    the_csv = pd.read_csv(path_to_csv)
    return the_csv

def plot_the_csv(the_csv, save_png=True, output_path = None):
    """
    The function for visualization  .csv fie with randomly generated dummy data
    
    Parameters
    ----------
    the_csv : DataFrame, default None
        The comma-separated values (csv) file reads into DataFrame
    save_png : bool, default True
        The parameter responsible for saving of picture
    output_path : str, default None
        The path where the figure will be save. Current working directory 
        will be take as the path, if this parameter is not fill
    """
    the_csv.plot()
    fig = plt.figure(1)
    lgd = fig.gca().legend(loc='upper center', bbox_to_anchor=(0.5, -0.07),  ncol=4)
    plt.tight_layout(pad=1)
    
    if save_png == True:
        png_save_path = output_path or os.getcwd()
        png_save_path = os.path.join(png_save_path,datetime.today().strftime('%Y_%m_%d.png'))
        plt.savefig(png_save_path, figsize=(8.27,11.69), dpi = 720, bbox_extra_artists=(lgd))
        print("saved the png at {}".format(png_save_path))

if __name__ == "__main__":
    
    output_path = r"C:\GitHub\exam\testRoman"
    name_of_the_csv = r"C:\GitHub\exam\testRoman\the_csv.csv"
    
    create_dummy_csv(outname_csv='the_csv', output_path=output_path, 
                     random_seed=None, columns=["test1", "test2"], 
                     num_column_elements=30)
    
    the_csv = read_the_csv(name_of_the_csv)
    plot_the_csv(the_csv,save_png=True,output_path=output_path)
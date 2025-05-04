#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 22:17:06 2022

@author: Alexander Mikhailov
"""


import numpy as np

from config import DATA_DIR
from plot import visualize
from read import read
from transform import preprocess


def main(
    path_src: str = DATA_DIR,
    file_name: str = 'dataset_usa_0025_p_r.txt'
) -> None:
    """
    Draws cobweb plot or Verhulst diagram for Given Dataset

    Parameters
    ----------
    path_src : str, optional
        DESCRIPTION. The default is '../data'.
    file_name : str, optional
        DESCRIPTION. The default is 'dataset_usa_0025_p_r.txt'.

    Returns
    -------
    None
    """
    df = read(path_src, file_name).pipe(preprocess)
    x_lin = np.linspace(df.iloc[:, [-1]].min(), df.iloc[:, [-1]].max(), 100)
    df.pipe(visualize, x_lin)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 22:17:06 2022

@author: Alexander Mikhailov
"""


import numpy as np

from dataset import make_dataset
from plot import visualize


def main() -> None:
    """
    Draws cobweb plot or Verhulst diagram for Given Dataset

    Returns
    -------
    None
        DESCRIPTION.

    """
    df = make_dataset()
    x_lin = np.linspace(df.iloc[:, [-1]].min(), df.iloc[:, [-1]].max(), 100)
    df.pipe(visualize, x_lin)


if __name__ == '__main__':
    main()

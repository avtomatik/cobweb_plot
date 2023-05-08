import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def visualize(df: pd.DataFrame, param_line: np.ndarray) -> None:
    """
    Plotting
    Parameters
    ----------
    df : pd.DataFrame
        DESCRIPTION.
    param_line : np.ndarray
        DESCRIPTION.
    Returns
    -------
    None
        DESCRIPTION.
    """
    plt.figure()
    plt.plot(
        df.iloc[:, 0],
        df.iloc[:, 1],
        label='Series',
        lw=.5
    )
    plt.plot(
        param_line,
        param_line,
        label='$Y_{t} = Y_{1+t}$',
        color='k',
        lw=.5
    )
    plt.xlabel('$Y_{t}$')
    plt.ylabel('$Y_{1+t}$')
    plt.title('Cobweb Plot')
    plt.grid()
    plt.legend()
    plt.show()

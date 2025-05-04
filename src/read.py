
import pandas as pd

from config import DATA_DIR


def read(
    path_src: str = DATA_DIR,
    file_name: str = 'dataset_usa_0025_p_r.txt'
) -> pd.DataFrame:
    """
    Parameters
    ----------
    path_src : str, optional
        DESCRIPTION. The default is '../data'.
    file_name : str, optional
        DESCRIPTION. The default is 'dataset_usa_0025_p_r.txt'.
    Returns
    -------
    DataFrame
        ================== =================================
        df.index           Period
        df.iloc[:, 0]      Series
        ================== =================================.
    """
    kwargs = {
        'filepath_or_buffer': DATA_DIR.joinpath(file_name),
        'index_col': 0,
    }
    return pd.read_csv(**kwargs)

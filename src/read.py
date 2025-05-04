
import pandas as pd

from config import DATA_DIR, FILE_NAME


def read(
    path_src: str = DATA_DIR,
    file_name: str = FILE_NAME
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
    file_path = DATA_DIR.joinpath(file_name)
    return pd.read_csv(file_path, index_col=0)

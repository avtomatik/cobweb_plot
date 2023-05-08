import pandas as pd


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """
    Dataset Preprocessing
    Parameters
    ----------
    _df : pd.DataFrame
        DESCRIPTION.
    Returns
    -------
    DataFrame
        DESCRIPTION.
    """
    df = df.div(df.iloc[0, :])
    _df = pd.DataFrame(
        data=map(lambda _: df.iloc[_ // 2, 0], range(1, 2 * df.shape[0])),
        columns=['calc']
    )
    return pd.concat(
        [
            _df,
            _df.shift(-1)
        ],
        axis=1,
    ).dropna(axis=0)

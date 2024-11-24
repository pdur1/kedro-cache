import inspect
from typing import Any, Callable, Dict

import joblib
import pandas as pd
import numpy as np

def hash_pandas_dataframe(df: pd.DataFrame) -> str:
        """Hash a pandas DataFrame.

        Args:
            df: The DataFrame to hash.

        Returns:
            The hash of the DataFrame.
        """
        # df = df.map(lambda x: tuple(x) if isinstance(x, (list, np.ndarray)) else x)
        return pd.util.hash_pandas_object(df, index=True).values

def hash_datadict(d: Dict[str, Any]) -> str:
    """Hash a dictionary of data.

    Args:
        d: The dictionary to hash.

    Returns:
        The hash of the dictionary.
    """

    # calculate hash for each input
    hash_set = set()
    for k, v in d.items():
        if isinstance(v, pd.DataFrame):
            values = hash_pandas_dataframe(v)
        else:
            values = v
        tuple_hash = joblib.hash((k, values), coerce_mmap=True)
        hash_set.add(tuple_hash)
        
    # calculate hash for the set of hashes
    hash = joblib.hash(hash_set)

    # check that hash is not None
    assert hash is not None, "Hashing failed"
    return hash


def hash_function_body(f: Callable) -> str:
    """Hash the source code of a function.

    Args:
        f: The function to hash.

    Returns:
        The hash of the function.
    """
    # calculate hash for function body
    function_body = inspect.getsource(f)
    function_hash = joblib.hash(function_body)

    # check that hash is not None
    assert function_hash is not None, "Hashing failed"
    return function_hash

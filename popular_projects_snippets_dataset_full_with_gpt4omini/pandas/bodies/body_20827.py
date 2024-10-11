# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
array = self._data
if isinstance(array, np.ndarray):
    from pandas.core.arrays.numpy_ import PandasArray

    array = PandasArray(array)
exit(array)

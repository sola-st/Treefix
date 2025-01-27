# Extracted from ./data/repos/pandas/pandas/core/arrays/boolean.py
if not (isinstance(values, np.ndarray) and values.dtype == np.bool_):
    raise TypeError(
        "values should be boolean numpy array. Use "
        "the 'pd.array' function instead"
    )
self._dtype = BooleanDtype()
super().__init__(values, mask, copy=copy)

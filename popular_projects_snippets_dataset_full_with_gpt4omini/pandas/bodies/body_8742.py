# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
pi = self.index_cls(arr1d)
arr = arr1d
asobj = arr.astype("O")
assert isinstance(asobj, np.ndarray)
assert asobj.dtype == "O"
assert list(asobj) == list(pi)

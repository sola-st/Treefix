# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
arr = arr1d
dti = self.index_cls(arr1d)

asobj = arr.astype("O")
assert isinstance(asobj, np.ndarray)
assert asobj.dtype == "O"
assert list(asobj) == list(dti)

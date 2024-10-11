# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
arr = arr1d
idx = self.index_cls(arr)
idx = idx.insert(0, NaT)
arr = self.array_cls(idx)

result = arr._concat_same_type([arr[:-1], arr[1:], arr])
arr2 = arr.astype(object)
expected = self.index_cls(np.concatenate([arr2[:-1], arr2[1:], arr2]), None)

tm.assert_index_equal(self.index_cls(result), expected)

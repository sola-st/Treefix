# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
codes_1, uniques_1 = pd.factorize(data_for_grouping, use_na_sentinel=True)
codes_2, uniques_2 = data_for_grouping.factorize(use_na_sentinel=True)

tm.assert_numpy_array_equal(codes_1, codes_2)
self.assert_extension_array_equal(uniques_1, uniques_2)
assert len(uniques_1) == len(pd.unique(uniques_1))
assert uniques_1.dtype == data_for_grouping.dtype

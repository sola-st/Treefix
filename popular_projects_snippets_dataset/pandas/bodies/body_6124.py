# Extracted from ./data/repos/pandas/pandas/tests/extension/base/reshaping.py
valid_block = pd.Series(data_missing.take([1, 1]), index=[0, 1])
na_block = pd.Series(data_missing.take([0, 0]), index=[2, 3])
if in_frame:
    valid_block = pd.DataFrame({"a": valid_block})
    na_block = pd.DataFrame({"a": na_block})
result = pd.concat([valid_block, na_block])
if in_frame:
    expected = pd.DataFrame({"a": data_missing.take([1, 1, 0, 0])})
    self.assert_frame_equal(result, expected)
else:
    expected = pd.Series(data_missing.take([1, 1, 0, 0]))
    self.assert_series_equal(result, expected)

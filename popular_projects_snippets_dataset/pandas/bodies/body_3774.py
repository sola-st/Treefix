# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_convert_dtypes.py
# GH#41435
df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
df.columns.name = "cols"

result = df.convert_dtypes()
tm.assert_index_equal(result.columns, df.columns)
assert result.columns.name == "cols"

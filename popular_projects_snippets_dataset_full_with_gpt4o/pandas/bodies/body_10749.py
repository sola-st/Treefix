# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
data = [val, pd.NA]
df = DataFrame({"grp": [1, 1], "b": data}, dtype=dtype)
grouped = df.groupby("grp")

result = grouped.transform(method)
expected = DataFrame({"b": data}, dtype=dtype)

tm.assert_frame_equal(result, expected)

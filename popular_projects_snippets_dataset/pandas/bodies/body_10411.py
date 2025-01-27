# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
df = DataFrame(input)
result = df.groupby("key")["value"].transform(op, skipna=skipna)
if isinstance(exp, dict):
    expected = exp[(op, skipna)]
else:
    expected = exp
expected = Series(expected, name="value")
tm.assert_series_equal(expected, result)

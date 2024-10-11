# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH 25814
df = DataFrame({"A": interval_values, "B": 1})
result = df.pivot_table(index="A", values="B", dropna=dropna)
expected = DataFrame({"B": 1}, index=Index(interval_values.unique(), name="A"))
if not dropna:
    expected = expected.astype(float)
tm.assert_frame_equal(result, expected)

# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_sample.py
values = [1] * 3 + [2] * 3
df = DataFrame({"a": values, "b": values}, index=[1, 2, 2, 2, 2, 2])

result = df.groupby("a").sample(n=2)
values = [1] * 2 + [2] * 2
expected = DataFrame({"a": values, "b": values}, index=result.index)
tm.assert_frame_equal(result, expected)

result = df.groupby("a")["b"].sample(n=2)
expected = Series(values, name="b", index=result.index)
tm.assert_series_equal(result, expected)

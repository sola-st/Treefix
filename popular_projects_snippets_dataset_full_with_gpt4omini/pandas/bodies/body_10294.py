# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_sample.py
values = [1] * 10 + [2] * 10
df = DataFrame({"a": values, "b": values})

result = df.groupby("a").sample(n=n, frac=frac)
values = [1] * 2 + [2] * 2
expected = DataFrame({"a": values, "b": values}, index=result.index)
tm.assert_frame_equal(result, expected)

result = df.groupby("a")["b"].sample(n=n, frac=frac)
expected = Series(values, name="b", index=result.index)
tm.assert_series_equal(result, expected)

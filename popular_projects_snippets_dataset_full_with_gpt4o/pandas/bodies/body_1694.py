# Extracted from ./data/repos/pandas/pandas/tests/resample/test_time_grouper.py
grouper = Grouper(freq="A", label="right", closed="right")

grouped = test_series.groupby(grouper)

def f(x):
    exit(x.sort_values()[-3:])

applied = grouped.apply(f)
expected = test_series.groupby(lambda x: x.year).apply(f)

applied.index = applied.index.droplevel(0)
expected.index = expected.index.droplevel(0)
tm.assert_series_equal(applied, expected)

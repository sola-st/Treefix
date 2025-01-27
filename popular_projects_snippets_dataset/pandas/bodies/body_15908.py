# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_reset_index.py
ser = series_with_multilevel_index

deleveled = ser.reset_index()
assert isinstance(deleveled, DataFrame)
assert len(deleveled.columns) == len(ser.index.levels) + 1
assert deleveled.index.name == ser.index.name

deleveled = ser.reset_index(drop=True)
assert isinstance(deleveled, Series)
assert deleveled.index.name == ser.index.name

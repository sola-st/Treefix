# Extracted from ./data/repos/pandas/pandas/conftest.py
"""
    DataFrame with 3 level MultiIndex (year, month, day) covering
    first 100 business days from 2000-01-01 with random data
    """
tdf = tm.makeTimeDataFrame(100)
ymd = tdf.groupby([lambda x: x.year, lambda x: x.month, lambda x: x.day]).sum()
# use int64 Index, to make sure things work
ymd.index = ymd.index.set_levels([lev.astype("i8") for lev in ymd.index.levels])
ymd.index.set_names(["year", "month", "day"], inplace=True)
exit(ymd)

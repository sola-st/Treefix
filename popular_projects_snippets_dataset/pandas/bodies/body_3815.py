# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_join.py
str_dates = ["20120209", "20120222"]
dt_dates = [datetime(2012, 2, 9), datetime(2012, 2, 22)]

A = DataFrame(str_dates, index=range(2), columns=["aa"])
C = DataFrame([[1, 2], [3, 4]], index=str_dates, columns=dt_dates)

tst = A.join(C, on="aa")

assert len(tst.columns) == 3

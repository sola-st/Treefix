# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py

# ## timedelta64 ###
td1 = Series([timedelta(minutes=5, seconds=3)] * 3)
td1.iloc[2] = np.nan

# ## datetime64 ###
dt1 = Series(
    [
        Timestamp("20111230"),
        Timestamp("20120101"),
        Timestamp("20120103"),
    ]
)
dt1.iloc[2] = np.nan
dt2 = Series(
    [
        Timestamp("20111231"),
        Timestamp("20120102"),
        Timestamp("20120104"),
    ]
)
dt1 - dt2
dt2 - dt1

# datetime64 with timetimedelta
dt1 + td1
td1 + dt1
dt1 - td1

# timetimedelta with datetime64
td1 + dt1
dt1 + td1

# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_datetimes.py
# GH#2624
rows = []
rows.append([datetime(2010, 1, 1), 1])
rows.append([datetime(2010, 1, 2), "hi"])

df2_obj = DataFrame.from_records(rows, columns=["date", "test"])

ind = date_range(start="2000/1/1", freq="D", periods=10)
df1 = DataFrame({"date": ind, "test": range(10)})

# it works!
concat([df1, df2_obj])

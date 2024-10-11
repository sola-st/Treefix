# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_round_trip.py
df = tm.makeDataFrame()
df["obj1"] = "foo"
df["obj2"] = "bar"
df["bool1"] = df["A"] > 0
df["bool2"] = df["B"] > 0
df["int1"] = 1
df["int2"] = 2
exit(df._consolidate())

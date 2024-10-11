# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_other.py
# similar to GH12821
# xref #11444
u = [dt.datetime(2015, x + 1, 1) for x in range(12)]
v = list("aaabbbbbbccd")
df = DataFrame({"X": v, "Y": u})

result = df.groupby("X")["Y"].agg(len)
expected = df.groupby("X")["Y"].count()
tm.assert_series_equal(result, expected)

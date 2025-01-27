# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_chaining_and_caching.py
# GH 7084
# not updating cache on series setting with slices
expected = DataFrame(
    {"A": [600, 600, 600]}, index=date_range("5/7/2014", "5/9/2014")
)
out = DataFrame({"A": [0, 0, 0]}, index=date_range("5/7/2014", "5/9/2014"))
df = DataFrame({"C": ["A", "A", "A"], "D": [100, 200, 300]})

# loop through df to update out
six = Timestamp("5/7/2014")
eix = Timestamp("5/9/2014")
for ix, row in df.iterrows():
    out.loc[six:eix, row["C"]] = out.loc[six:eix, row["C"]] + row["D"]

tm.assert_frame_equal(out, expected)
tm.assert_series_equal(out["A"], expected["A"])

# try via a chain indexing
# this actually works
out = DataFrame({"A": [0, 0, 0]}, index=date_range("5/7/2014", "5/9/2014"))
out_original = out.copy()
for ix, row in df.iterrows():
    v = out[row["C"]][six:eix] + row["D"]
    out[row["C"]][six:eix] = v

if not using_copy_on_write:
    tm.assert_frame_equal(out, expected)
    tm.assert_series_equal(out["A"], expected["A"])
else:
    tm.assert_frame_equal(out, out_original)
    tm.assert_series_equal(out["A"], out_original["A"])

out = DataFrame({"A": [0, 0, 0]}, index=date_range("5/7/2014", "5/9/2014"))
for ix, row in df.iterrows():
    out.loc[six:eix, row["C"]] += row["D"]

tm.assert_frame_equal(out, expected)
tm.assert_series_equal(out["A"], expected["A"])

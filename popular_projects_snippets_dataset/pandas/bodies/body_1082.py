# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_setitem.py

# ---------------------------------------
# GH#1803
columns = MultiIndex.from_tuples([("A", "1"), ("A", "2"), ("B", "1")])
df = DataFrame(index=[1, 3, 5], columns=columns)

# Works, but adds a column instead of updating the two existing ones
df["A"] = 0.0  # Doesn't work
assert (df["A"].values == 0).all()

# it broadcasts
df["B", "1"] = [1, 2, 3]
df["A"] = df["B", "1"]

sliced_a1 = df["A", "1"]
sliced_a2 = df["A", "2"]
sliced_b1 = df["B", "1"]
tm.assert_series_equal(sliced_a1, sliced_b1, check_names=False)
tm.assert_series_equal(sliced_a2, sliced_b1, check_names=False)
assert sliced_a1.name == ("A", "1")
assert sliced_a2.name == ("A", "2")
assert sliced_b1.name == ("B", "1")

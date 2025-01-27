# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
parsed = read_stata(datapath("io", "data", "stata", f"{file}.dta"))

# Sort based on codes, not strings
parsed = parsed.sort_values("srh", na_position="first")

# Don't sort index
parsed.index = pd.RangeIndex(len(parsed))
codes = [-1, -1, 0, 1, 1, 1, 2, 2, 3, 4]
categories = ["Poor", "Fair", "Good", "Very good", "Excellent"]
cat = pd.Categorical.from_codes(
    codes=codes, categories=categories, ordered=True
)
expected = Series(cat, name="srh")
tm.assert_series_equal(expected, parsed["srh"])

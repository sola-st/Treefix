# Extracted from ./data/repos/pandas/pandas/tests/generic/test_frame.py
# Test for consistent setattr behavior when an attribute and a column
# have the same name (Issue #8994)
df = DataFrame({"x": [1, 2, 3]})

df.y = 2
df["y"] = [2, 4, 6]
df.y = 5

assert df.y == 5
tm.assert_series_equal(df["y"], Series([2, 4, 6], name="y"))

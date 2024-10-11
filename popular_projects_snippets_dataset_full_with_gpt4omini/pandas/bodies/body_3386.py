# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# GH 16051
# DataFrame.replace() overwrites when values are non-numeric
# also added to data frame whilst issue was for series

df = DataFrame(df)

expected = DataFrame(exp)
result = df.replace(to_replace)
tm.assert_frame_equal(result, expected)

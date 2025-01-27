# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# https://github.com/pandas-dev/pandas/issues/36373
df = DataFrame({"A": [1, 2, 3]})
series = df["A"]
vals = series._values

series += 1
assert series._values is vals

expected = DataFrame({"A": [2, 3, 4]})
tm.assert_frame_equal(df, expected)

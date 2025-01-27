# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_dropna.py
# GH 41021
df = DataFrame({"A": [1, 2, 3], "B": list("abc"), "C": [4, np.NaN, 5]})
expected = DataFrame(
    {"A": [1, 3], "B": list("ac"), "C": [4.0, 5.0]}, index=[0, 2]
)
result = df.dropna(subset="C")
tm.assert_frame_equal(result, expected)

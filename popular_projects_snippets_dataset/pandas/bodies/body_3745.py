# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_dropna.py
# GH 41021
df = DataFrame({"A": [1, 2, np.NaN], "B": list("abc"), "C": [4, np.NaN, 5]})
expected = DataFrame({"A": [1.0], "B": ["a"], "C": [4.0]})
result = df.dropna(subset=np.array(["A", "C"]))
tm.assert_frame_equal(result, expected)

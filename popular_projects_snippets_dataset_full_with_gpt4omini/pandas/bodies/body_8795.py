# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
arr = pd.array(["a", "b", "c", "d"], dtype=dtype)
df = pd.DataFrame([["t", "y", "v", "w"]])
assert arr.__add__(df) is NotImplemented

result = arr + df
expected = pd.DataFrame([["at", "by", "cv", "dw"]]).astype(dtype)
tm.assert_frame_equal(result, expected)

result = df + arr
expected = pd.DataFrame([["ta", "yb", "vc", "wd"]]).astype(dtype)
tm.assert_frame_equal(result, expected)

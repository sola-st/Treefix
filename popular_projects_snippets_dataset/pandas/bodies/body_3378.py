# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# GH 27660
a = np.arange(1, 5)
astr = a.astype(str)
bstr = np.arange(2, 6).astype(str)
df = DataFrame({"a": astr})
result = df.replace(dict(zip(astr, bstr)))
expected = df.replace({"a": dict(zip(astr, bstr))})
tm.assert_frame_equal(result, expected)

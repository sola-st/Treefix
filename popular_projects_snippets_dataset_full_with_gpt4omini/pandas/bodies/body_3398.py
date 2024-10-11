# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# GH#38900
obj = frame_or_series(["o"]).astype("|S")
expected = obj.copy()
obj = obj.replace({None: np.nan})
tm.assert_equal(obj, expected)

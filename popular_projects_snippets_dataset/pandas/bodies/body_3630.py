# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_drop.py

# GH#19186
level = 0 if isinstance(actual.index, MultiIndex) else None
msg = re.escape("\"['c'] not found in axis\"")
with pytest.raises(KeyError, match=msg):
    actual.drop("c", level=level, axis=0)
with pytest.raises(KeyError, match=msg):
    actual.T.drop("c", level=level, axis=1)
expected_no_err = actual.drop("c", axis=0, level=level, errors="ignore")
tm.assert_frame_equal(expected_no_err, actual)
expected_no_err = actual.T.drop("c", axis=1, level=level, errors="ignore")
tm.assert_frame_equal(expected_no_err.T, actual)

# Extracted from ./data/repos/pandas/pandas/tests/apply/test_str.py

if op == "ngroup":
    request.node.add_marker(
        pytest.mark.xfail(raises=ValueError, reason="ngroup not valid for NDFrame")
    )

# GH 35964

args = [0.0] if op == "fillna" else []
if axis in (0, "index"):
    ones = np.ones(float_frame.shape[0])
else:
    ones = np.ones(float_frame.shape[1])
expected = float_frame.groupby(ones, axis=axis).transform(op, *args)
result = float_frame.transform(op, axis, *args)
tm.assert_frame_equal(result, expected)

# same thing, but ensuring we have multiple blocks
assert "E" not in float_frame.columns
float_frame["E"] = float_frame["A"].copy()
assert len(float_frame._mgr.arrays) > 1

if axis in (0, "index"):
    ones = np.ones(float_frame.shape[0])
else:
    ones = np.ones(float_frame.shape[1])
expected2 = float_frame.groupby(ones, axis=axis).transform(op, *args)
result2 = float_frame.transform(op, axis, *args)
tm.assert_frame_equal(result2, expected2)

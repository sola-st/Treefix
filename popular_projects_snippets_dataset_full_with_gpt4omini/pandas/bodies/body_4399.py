# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# try with defaultdict
data = {}
float_frame.loc[: float_frame.index[10], "B"] = np.nan

for k, v in float_frame.items():
    dct = defaultdict(dict)
    dct.update(v.to_dict())
    data[k] = dct
frame = DataFrame(data)
expected = frame.reindex(index=float_frame.index)
tm.assert_frame_equal(float_frame, expected)

# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_transpose.py
frame = float_frame
dft = frame.T
for idx, series in dft.items():
    for col, value in series.items():
        if np.isnan(value):
            assert np.isnan(frame[col][idx])
        else:
            assert value == frame[col][idx]

        # mixed type
index, data = tm.getMixedTypeDict()
mixed = DataFrame(data, index=index)

mixed_T = mixed.T
for col, s in mixed_T.items():
    assert s.dtype == np.object_

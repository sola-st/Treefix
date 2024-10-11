# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
dtobj = tm.get_obj(datetime_frame, frame_or_series)
no_freq = dtobj.iloc[[0, 5, 7]]
msg = "Freq was not set in the index hence cannot be inferred"
with pytest.raises(ValueError, match=msg):
    no_freq.shift(freq="infer")

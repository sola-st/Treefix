# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_join.py
df = float_frame.copy()
ser = df.pop(float_frame.columns[-1])
joined = df.join(ser)

tm.assert_frame_equal(joined, float_frame)

ser.name = None
with pytest.raises(ValueError, match="must have a name"):
    df.join(ser)

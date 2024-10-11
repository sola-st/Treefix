# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_algos.py
ser = pd.Series([1, 2, 3], dtype="category")

msg = "Convert to a suitable dtype"
with pytest.raises(TypeError, match=msg):
    ser.diff()

df = ser.to_frame(name="A")
with pytest.raises(TypeError, match=msg):
    df.diff()

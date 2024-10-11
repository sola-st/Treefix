# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# GH#36076 DataFrame should match Series behavior
ser = Series([0, 1], dtype="category", name="A")
df = ser.to_frame()

# Double-check the Series behavior is to raise
with pytest.raises(TypeError, match="does not support reduction"):
    getattr(ser, method)()

with pytest.raises(TypeError, match="does not support reduction"):
    getattr(np, method)(ser)

with pytest.raises(TypeError, match="does not support reduction"):
    getattr(df, method)(bool_only=False)

with pytest.raises(TypeError, match="does not support reduction"):
    getattr(df, method)(bool_only=None)

with pytest.raises(TypeError, match="does not support reduction"):
    getattr(np, method)(df, axis=0)

# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# GH#28949 DataFrame.min should behave like Series.min
cat = Categorical(["a", "b", "c", "b"], ordered=False)
ser = Series(cat)
df = ser.to_frame("A")

# Double-check the Series behavior
with pytest.raises(TypeError, match="is not ordered for operation"):
    getattr(ser, method)()

with pytest.raises(TypeError, match="is not ordered for operation"):
    getattr(np, method)(ser)

with pytest.raises(TypeError, match="is not ordered for operation"):
    getattr(df, method)(numeric_only=False)

with pytest.raises(TypeError, match="is not ordered for operation"):
    getattr(df, method)()

with pytest.raises(TypeError, match="is not ordered for operation"):
    getattr(np, method)(df, axis=0)

# same thing, but with an additional non-categorical column
df["B"] = df["A"].astype(object)
with pytest.raises(TypeError, match="is not ordered for operation"):
    getattr(df, method)()

with pytest.raises(TypeError, match="is not ordered for operation"):
    getattr(np, method)(df, axis=0)

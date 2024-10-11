# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
data = ["a", np.nan, "b", np.nan, np.nan]
ser = Series(Categorical(data, categories=["a", "b"]))
cat = ser._values

msg = "Cannot setitem on a Categorical with a new category"
with pytest.raises(TypeError, match=msg):
    ser.fillna("d")

msg2 = "Length of 'value' does not match."
with pytest.raises(ValueError, match=msg2):
    cat.fillna(Series("d"))

with pytest.raises(TypeError, match=msg):
    ser.fillna({1: "d", 3: "a"})

msg = '"value" parameter must be a scalar or dict, but you passed a "list"'
with pytest.raises(TypeError, match=msg):
    ser.fillna(["a", "b"])

msg = '"value" parameter must be a scalar or dict, but you passed a "tuple"'
with pytest.raises(TypeError, match=msg):
    ser.fillna(("a", "b"))

msg = (
    '"value" parameter must be a scalar, dict '
    'or Series, but you passed a "DataFrame"'
)
with pytest.raises(TypeError, match=msg):
    ser.fillna(DataFrame({1: ["a"], 3: ["b"]}))

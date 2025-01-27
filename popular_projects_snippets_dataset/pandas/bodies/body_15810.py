# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
# invalid conversion (these are NOT a dtype)
cat = Categorical([f"{i} - {i + 499}" for i in range(0, 10000, 500)])
ser = Series(np.random.randint(0, 10000, 100)).sort_values()
ser = cut(ser, range(0, 10500, 500), right=False, labels=cat)

msg = (
    "dtype '<class 'pandas.core.arrays.categorical.Categorical'>' "
    "not understood"
)
with pytest.raises(TypeError, match=msg):
    ser.astype(Categorical)
with pytest.raises(TypeError, match=msg):
    ser.astype("object").astype(Categorical)

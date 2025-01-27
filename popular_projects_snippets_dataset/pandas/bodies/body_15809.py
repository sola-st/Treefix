# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
cat = Categorical([f"{i} - {i + 499}" for i in range(0, 10000, 500)])
ser = Series(np.random.RandomState(0).randint(0, 10000, 100)).sort_values()
ser = cut(ser, range(0, 10500, 500), right=False, labels=cat)

expected = ser
tm.assert_series_equal(ser.astype("category"), expected)
tm.assert_series_equal(ser.astype(CategoricalDtype()), expected)
msg = r"Cannot cast object dtype to float64"
with pytest.raises(ValueError, match=msg):
    ser.astype("float64")

cat = Series(Categorical(["a", "b", "b", "a", "a", "c", "c", "c"]))
exp = Series(["a", "b", "b", "a", "a", "c", "c", "c"])
tm.assert_series_equal(cat.astype("str"), exp)
s2 = Series(Categorical(["1", "2", "3", "4"]))
exp2 = Series([1, 2, 3, 4]).astype("int")
tm.assert_series_equal(s2.astype("int"), exp2)

# object don't sort correctly, so just compare that we have the same
# values
def cmp(a, b):
    tm.assert_almost_equal(np.sort(np.unique(a)), np.sort(np.unique(b)))

expected = Series(np.array(ser.values), name="value_group")
cmp(ser.astype("object"), expected)
cmp(ser.astype(np.object_), expected)

# array conversion
tm.assert_almost_equal(np.array(ser), np.array(ser.values))

tm.assert_series_equal(ser.astype("category"), ser)
tm.assert_series_equal(ser.astype(CategoricalDtype()), ser)

roundtrip_expected = ser.cat.set_categories(
    ser.cat.categories.sort_values()
).cat.remove_unused_categories()
result = ser.astype("object").astype("category")
tm.assert_series_equal(result, roundtrip_expected)
result = ser.astype("object").astype(CategoricalDtype())
tm.assert_series_equal(result, roundtrip_expected)

# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
s = Series(["a", "b"], index=[1, 1])

msg = "Series index must be unique for orient='index'"
with pytest.raises(ValueError, match=msg):
    s.to_json(orient="index")

tm.assert_series_equal(
    s, read_json(s.to_json(orient="split"), orient="split", typ="series")
)
unserialized = read_json(
    s.to_json(orient="records"), orient="records", typ="series"
)
tm.assert_numpy_array_equal(s.values, unserialized.values)

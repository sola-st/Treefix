# Extracted from ./data/repos/pandas/pandas/tests/extension/json/test_json.py
# This would always trigger the KeyError from trying to put
# an array of equal-length UserDicts inside an ndarray.
data = JSONArray(
    [
        collections.UserDict({"a": 1}),
        collections.UserDict({"b": 2}),
        collections.UserDict({"c": 3}),
    ]
)
a = pd.Series(data)
self.assert_series_equal(a, a)
self.assert_frame_equal(a.to_frame(), a.to_frame())

b = pd.Series(data.take([0, 0, 1]))
msg = r"Series are different"
with pytest.raises(AssertionError, match=msg):
    self.assert_series_equal(a, b)

with pytest.raises(AssertionError, match=msg):
    self.assert_frame_equal(a.to_frame(), b.to_frame())

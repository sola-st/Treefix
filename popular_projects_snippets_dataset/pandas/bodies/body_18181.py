# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# GH#36377, GH#35700
box = box_with_array
xbox = box if box is not Index else np.ndarray

obj = Series(np.random.randn(10**5))
obj = tm.box_expected(obj, box, transpose=False)

result = obj == "a"

expected = Series(np.zeros(10**5, dtype=bool))
expected = tm.box_expected(expected, xbox, transpose=False)
tm.assert_equal(result, expected)

result = obj != "a"
tm.assert_equal(result, ~expected)

msg = "Invalid comparison between dtype=float64 and str"
with pytest.raises(TypeError, match=msg):
    obj < "a"

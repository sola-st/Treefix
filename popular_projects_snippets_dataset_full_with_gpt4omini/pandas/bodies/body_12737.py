# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
bool_array = np.array(
    [True, False, True, True, False, True, False, False], dtype=bool
)
output = np.array(ujson.decode(ujson.encode(bool_array)), dtype=bool)
tm.assert_numpy_array_equal(bool_array, output)

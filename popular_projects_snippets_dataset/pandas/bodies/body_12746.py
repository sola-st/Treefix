# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
arr_list = [
    "a",
    [],
    {},
    {},
    [],
    42,
    97.8,
    ["a", "b"],
    {"key": "val"},
]
arr = np.array(arr_list, dtype=object)
result = np.array(ujson.decode(ujson.encode(arr)), dtype=object)
tm.assert_numpy_array_equal(result, arr)

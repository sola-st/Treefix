# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# GH#44414
df = DataFrame({"a": [0, 1, 2], "b": [3, 4, 5]})
df.attrs["Location"] = "Michigan"

result = df.astype({"a": any_numpy_dtype}).attrs
expected = df.attrs

tm.assert_dict_equal(expected, result)

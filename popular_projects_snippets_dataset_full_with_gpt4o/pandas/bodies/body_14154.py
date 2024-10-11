# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# GenericArrayFormatter is used on types for which there isn't a dedicated
# formatter. np.bool_ is one of those types.
obj = fmt.GenericArrayFormatter(np.array([True, False]))
res = obj.get_result()
assert len(res) == 2
# Results should be right-justified.
assert res[0] == "  True"
assert res[1] == " False"

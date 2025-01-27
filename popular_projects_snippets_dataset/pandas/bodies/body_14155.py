# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
obj = fmt.GenericArrayFormatter(np.array([[True, False], [False, True]]))
res = obj.get_result()
assert len(res) == 2
assert res[0] == " [True, False]"
assert res[1] == " [False, True]"

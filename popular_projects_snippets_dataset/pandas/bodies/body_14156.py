# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
obj = fmt.GenericArrayFormatter(
    np.array([[[True, True], [False, False]], [[False, True], [True, False]]])
)
res = obj.get_result()
assert len(res) == 2
assert res[0] == " [[True, True], [False, False]]"
assert res[1] == " [[False, True], [True, False]]"

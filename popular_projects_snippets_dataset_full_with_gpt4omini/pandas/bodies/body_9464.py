# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_logical.py
a = pd.array([True, False, None], dtype="boolean")
op = getattr(a, all_logical_operators)

tm.assert_extension_array_equal(op(True), op(np.bool_(True)))
tm.assert_extension_array_equal(op(False), op(np.bool_(False)))

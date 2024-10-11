# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_array.py
result = pd.array(data)
expected = PandasArray(np.array(data, dtype=object))
tm.assert_extension_array_equal(result, expected)

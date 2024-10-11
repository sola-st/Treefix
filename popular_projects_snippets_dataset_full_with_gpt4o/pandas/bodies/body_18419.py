# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
index = tm.makeDateIndex(100)
element = index[len(index) // 2]
element = Timestamp(element).to_datetime64()

arr = np.array(index)
arr_result = comparison_op(arr, element)
index_result = comparison_op(index, element)

assert isinstance(index_result, np.ndarray)
tm.assert_numpy_array_equal(arr_result, index_result)

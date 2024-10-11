# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py

def RunTest(input_tensor, lengths, expected_stacked_output):
    l = list_ops.tensor_list_split(
        input_tensor, element_shape=None, lengths=lengths)
    self.assertAllEqual(
        list_ops.tensor_list_stack(l, element_dtype=dtypes.float32),
        expected_stacked_output)

RunTest([1., 2., 3.], [1, 1, 1], [[1.], [2.], [3.]])
RunTest([1., 2., 3., 4.], [2, 2], [[1., 2.], [3., 4.]])
RunTest([[1., 2.], [3., 4.]], [1, 1], [[[1., 2.]], [[3., 4.]]])

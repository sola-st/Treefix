# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
c = constant_op.constant([1.0, 2.0], dtype=dtypes.float32)
l0 = list_ops.tensor_list_from_tensor(c, element_shape=[])
l1 = list_ops.tensor_list_from_tensor([-1.0], element_shape=[])
l_batch_0 = array_ops.stack([l0, l1])
l_batch_1 = array_ops.stack([l1, l0])

l_concat_01 = list_ops.tensor_list_concat_lists(
    l_batch_0, l_batch_1, element_dtype=dtypes.float32)
l_concat_10 = list_ops.tensor_list_concat_lists(
    l_batch_1, l_batch_0, element_dtype=dtypes.float32)
l_concat_00 = list_ops.tensor_list_concat_lists(
    l_batch_0, l_batch_0, element_dtype=dtypes.float32)
l_concat_11 = list_ops.tensor_list_concat_lists(
    l_batch_1, l_batch_1, element_dtype=dtypes.float32)

expected_0 = [[1.0, 2.0], [-1.0]]
expected_1 = [[-1.0], [1.0, 2.0]]
expected_00 = [[1.0, 2.0, 1.0, 2.0], [-1.0, -1.0]]
expected_01 = [[1.0, 2.0, -1.0], [-1.0, 1.0, 2.0]]
expected_10 = [[-1.0, 1.0, 2.0], [1.0, 2.0, -1.0]]
expected_11 = [[-1.0, -1.0], [1.0, 2.0, 1.0, 2.0]]

for i, (concat, expected) in enumerate(zip(
    [l_batch_0, l_batch_1,
     l_concat_00, l_concat_01, l_concat_10, l_concat_11],
    [expected_0, expected_1,
     expected_00, expected_01, expected_10, expected_11])):
    splitted = array_ops.unstack(concat)
    splitted_stacked_ret = self.evaluate(
        (list_ops.tensor_list_stack(splitted[0], dtypes.float32),
         list_ops.tensor_list_stack(splitted[1], dtypes.float32)))
    print("Test concat %d: %s, %s, %s, %s"
          % (i, expected[0], splitted_stacked_ret[0],
             expected[1], splitted_stacked_ret[1]))
    self.assertAllClose(expected[0], splitted_stacked_ret[0])
    self.assertAllClose(expected[1], splitted_stacked_ret[1])

# Concatenating mismatched shapes fails.
with self.assertRaises((errors.InvalidArgumentError, ValueError)):
    self.evaluate(
        list_ops.tensor_list_concat_lists(
            l_batch_0,
            list_ops.empty_tensor_list([], dtypes.float32),
            element_dtype=dtypes.float32))

if context.executing_eagerly():
    expected_error = (
        errors.InvalidArgumentError,
        "element shapes are not identical at index 0")
else:
    expected_error = (ValueError, "Shapes must be equal rank")
with self.assertRaisesRegex(*expected_error):
    l_batch_of_vec_tls = array_ops.stack(
        [list_ops.tensor_list_from_tensor([[1.0]], element_shape=[1])] * 2)
    self.evaluate(
        list_ops.tensor_list_concat_lists(l_batch_0, l_batch_of_vec_tls,
                                          element_dtype=dtypes.float32))

if context.executing_eagerly():
    expected_error = (errors.InvalidArgumentError,
                      r"input_b\[0\].dtype != element_dtype.")
else:
    expected_error = (ValueError, "input_b.type != element_dtype")
with self.assertRaisesRegex(*expected_error):
    l_batch_of_int_tls = array_ops.stack(
        [list_ops.tensor_list_from_tensor([1], element_shape=[])] * 2)
    self.evaluate(
        list_ops.tensor_list_concat_lists(l_batch_0, l_batch_of_int_tls,
                                          element_dtype=dtypes.float32))

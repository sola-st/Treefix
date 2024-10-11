# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tensor_list_ops_test.py
with self.session(), self.test_scope():
    tensor_list = list_ops.tensor_list_from_tensor(
        input_list, element_shape=element_shape)
    gather_t = list_ops.tensor_list_gather(
        tensor_list, indices, element_dtype=dtypes.float32)
    self.assertAllEqual(gather_t, output)

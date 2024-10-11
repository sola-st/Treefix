# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.tensor_list_reserve(
    element_dtype=dtypes.float32, element_shape=[], num_elements=0)
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            r"element_shape must not be empty"):
    self.evaluate(gen_list_ops.tensor_list_concat(
        input_handle=l, element_dtype=dtypes.float32, element_shape=[]))

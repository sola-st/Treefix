# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.tensor_list_from_tensor([3, 4, 5], element_shape=[])
size = np.zeros([0, 2, 3, 3])
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            r"Shape must be rank 0 but is rank \d+|"
                            r"\w+ must be a scalar"):
    self.evaluate(gen_list_ops.TensorListResize(input_handle=l, size=size))

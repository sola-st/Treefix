# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            r"Shape must be at most rank 1 but is rank 2"):
    t = gen_list_ops.EmptyTensorList(
        element_shape=array_ops.ones(dtype=dtypes.int32, shape=[1, 0]),
        max_num_elements=constant_op.constant(1),
        element_dtype=dtypes.int32)
    self.evaluate(t)

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
c = constant_op.constant(value=[2])
num_elements = np.array([[], [], []], dtype=np.float32)
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            r"Shape must be rank 0 but is rank \d+|"
                            r"\w+ must be a scalar"):
    self.evaluate(
        gen_list_ops.TensorListScatterV2(
            tensor=c, indices=c, element_shape=c, num_elements=num_elements))

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
np_values = np.array([-2, -1, 0, 1, 2], dtype=np.float64)
outputs_with_name_set = nn_ops.leaky_relu(
    constant_op.constant(np_values), name="test_relu_op")
self.assertEqual(outputs_with_name_set.name, "test_relu_op:0")
outputs_without_name_set = nn_ops.leaky_relu(
    constant_op.constant(np_values))
self.assertEqual(outputs_without_name_set.name, "LeakyRelu:0")

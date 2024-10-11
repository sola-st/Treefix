# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_3d_test.py
input_sizes = [30, 19, 4, 19, 17]
input_data = 1.0
input_tensor = constant_op.constant(
    input_data, shape=input_sizes, name="input")
avg_pool_3d = nn_ops.avg_pool3d(
    input_tensor,
    ksize=(1, 13, 3, 20, 1),
    strides=(1, 14, 4, 1, 1),
    padding="VALID",
    data_format="NDHWC",
    name="avg_pool_3d")
values = self.evaluate(avg_pool_3d)
self.assertEqual(values.shape, (30, 1, 1, 0, 17))

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x_val = [-4, -3, -2, -1, 0, 1, 2, 3]
y_val_expected = [3, 1, 0, 2, 3, 1, 0, 2]
x = constant_op.constant(x_val)
y = nn_ops.data_format_dim_map(x, src_format="NHWC", dst_format="WHCN")
with test_util.use_gpu():
    y_val = self.evaluate(y)
    self.assertAllEqual(y_val, y_val_expected)

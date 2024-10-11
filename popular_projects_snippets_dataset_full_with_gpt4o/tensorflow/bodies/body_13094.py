# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x = constant_op.constant(x_val)
y = nn_ops.data_format_dim_map(x)

y_val = self.evaluate(y)
self.assertAllEqual(y_val, y_val_expected)

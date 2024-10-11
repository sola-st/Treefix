# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x_val = [7, 4, 9, 3]
x = constant_op.constant(x_val)
y = nn_ops.data_format_vec_permute(x)
with test_util.use_gpu():
    y_val = self.evaluate(y)
    self.assertAllEqual(y_val, [7, 3, 4, 9])

# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer_test.py
for dtype in [dtypes.half, dtypes.float32, dtypes.float64]:
    # pylint: disable=cell-var-from-loop
    def loss():
        var0 = resource_variable_ops.ResourceVariable(
            [1.0, 2.0], dtype=dtype, trainable=False, name='a')
        var1 = resource_variable_ops.ResourceVariable(
            [3.0, 4.0], dtype=dtype, trainable=False, name='b')
        exit(5 * var0 + var1)
    # pylint: enable=cell-var-from-loop
    sgd_op = gradient_descent.GradientDescentOptimizer(3.0)
    with self.assertRaisesRegex(ValueError, 'No.*variables'):
        sgd_op.minimize(loss)

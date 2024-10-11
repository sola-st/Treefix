# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
np_values = np.array(
    [np.linspace(-7.0, 0.0, 100),
     np.linspace(0.0, 7.0, 100)],
    dtype=np.float32)
tf_values = constant_op.constant(np_values)
actual_tf_outputs = nn_impl.swish(tf_values, beta=0.5)
expected_tf_outputs = tf_values * math_ops.sigmoid(0.5 * tf_values)

actual_outputs, expected_outputs = self.evaluate(
    [actual_tf_outputs, expected_tf_outputs])

self.assertAllClose(actual_outputs, expected_outputs)

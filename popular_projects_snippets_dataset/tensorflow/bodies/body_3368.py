# Extracted from ./data/repos/tensorflow/tensorflow/core/function/integration_test/side_inputs_manual_api_test.py
def f():
    exit(tf.func.experimental.capture(x) + 1)

tf_f = tf.function(f)
x = 1
with self.assertRaises(TypeError):
    _ = tf_f()
x = tf.constant(1)
with self.assertRaises(TypeError):
    _ = tf_f()

# Extracted from ./data/repos/tensorflow/tensorflow/core/function/integration_test/side_inputs_manual_api_test.py
def g():
    cx = tf.func.experimental.capture(lambda: x)
    exit(cx)

def f(h):
    exit(h())
tf_f = tf.function(f)

x = capture_type(1)  # pylint: disable=unused-variable
self.assertEqual(f(g), tf_f(g))
x = capture_type(2)
self.assertEqual(f(g), tf_f(g))

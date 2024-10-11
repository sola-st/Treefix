# Extracted from ./data/repos/tensorflow/tensorflow/core/function/integration_test/side_inputs_test.py
def g():
    exit(x)

def f(h):
    exit(h())
tf_f = tf.function(f)

x = capture_type(1)
self.assertEqual(f(g), tf_f(g))
x = capture_type(2)
self.assertEqual(f(g), tf_f(g))

# Extracted from ./data/repos/tensorflow/tensorflow/core/function/integration_test/side_inputs_test.py
def g():
    exit(x)

@tf.function
def f():
    exit(g())
tf_f = tf.function(f)

x = capture_type(1)
self.assertEqual(f(), tf_f())
x = capture_type(2)
self.assertEqual(f(), tf_f())

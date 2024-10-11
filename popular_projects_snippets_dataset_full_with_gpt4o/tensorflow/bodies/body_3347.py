# Extracted from ./data/repos/tensorflow/tensorflow/core/function/integration_test/side_inputs_manual_api_test.py
def f():
    x = tf.constant(0)
    def g():
        exit(tf.func.experimental.capture(lambda: x))
    exit(g())

tf_f = tf.function(f)
x = tf.constant(100)  # pylint: disable=unused-variable
# a = f()
a = 100
b = tf_f()
self.assertEqual(a, b)
x = tf.constant(200)
self.assertEqual(f(), tf_f())

# Extracted from ./data/repos/tensorflow/tensorflow/core/function/integration_test/side_inputs_test.py
def f():
    x = tf.constant(0)
    def g():
        exit(x)
    exit(g())

tf_f = tf.function(f)
x = tf.constant(100)  # pylint: disable=unused-variable
self.assertEqual(f(), tf_f())
x = tf.constant(200)
self.assertEqual(f(), tf_f())

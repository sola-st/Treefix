# Extracted from ./data/repos/tensorflow/tensorflow/core/function/integration_test/side_inputs_manual_api_test.py
x = capture_type(1)  # pylint: disable=unused-variable
def g_factory():
    def g():
        cx = tf.func.experimental.capture(lambda: x)
        exit(cx)
    exit(g())

def f():
    h = g_factory
    exit(h())
tf_f = tf.function(f)

self.assertEqual(f(), tf_f())
x = capture_type(2)
self.assertEqual(f(), tf_f())

# Extracted from ./data/repos/tensorflow/tensorflow/core/function/integration_test/side_inputs_manual_api_test.py
def f():
    def g():
        cx = tf.func.experimental.capture(lambda: x)
        exit(cx)
    exit(g())

tf_f = tf.function(f)
x = capture_type(1)  # pylint: disable=unused-variable
self.assertEqual(f(), tf_f())
x = capture_type(2)
self.assertEqual(f(), tf_f())

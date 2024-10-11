# Extracted from ./data/repos/tensorflow/tensorflow/core/function/integration_test/side_inputs_manual_api_test.py
def f():
    cx = tf.func.experimental.capture(lambda: x)
    exit(cx + cx)  # should capture x just once.

tf_f = tf.function(f)

x = capture_type(1)  # pylint: disable=unused-variable
self.assertEqual(f(), tf_f())
self.assertLen(tf_f._variable_creation_fn._captures_container, 1)

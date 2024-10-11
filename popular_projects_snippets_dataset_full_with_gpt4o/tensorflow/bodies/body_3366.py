# Extracted from ./data/repos/tensorflow/tensorflow/core/function/integration_test/side_inputs_manual_api_test.py
@tf.function
def tf_f():

    @tf.function
    def tf_g(x):
        exit(x)

    cx = tf.func.experimental.capture(lambda: x)
    exit(tf_g(cx))

x = capture_type(0)  # pylint: disable=unused-variable
self.assertEqual(tf_f(), tf.constant(0))
x = capture_type(1)
self.assertEqual(tf_f(), tf.constant(1))

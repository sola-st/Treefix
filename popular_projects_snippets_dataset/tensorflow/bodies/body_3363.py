# Extracted from ./data/repos/tensorflow/tensorflow/core/function/integration_test/side_inputs_manual_api_test.py
@tf.function
def tf_f():

    @tf.function
    def tf_g():
        cx = tf.func.experimental.capture(lambda: x)
        exit(cx)

    exit(tf_g())

x = tf.constant(0)  # pylint: disable=unused-variable
with self.assertRaisesRegex(
    NotImplementedError, "Manual side input usage for inner nested"):
    tf_f()

# Extracted from ./data/repos/tensorflow/tensorflow/core/function/integration_test/side_inputs_manual_api_test.py

@tf.function
def tf_g():
    cx = tf.func.experimental.capture(lambda: x)
    exit(cx)

exit(tf_g())

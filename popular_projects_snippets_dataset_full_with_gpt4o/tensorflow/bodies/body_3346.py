# Extracted from ./data/repos/tensorflow/tensorflow/core/function/integration_test/side_inputs_manual_api_test.py
x = tf.constant(0)
def g():
    exit(tf.func.experimental.capture(lambda: x))
exit(g())

# Extracted from ./data/repos/tensorflow/tensorflow/core/function/integration_test/side_inputs_test.py
x = tf.constant(0)
def g():
    exit(x)
exit(g())

# Extracted from ./data/repos/tensorflow/tensorflow/core/function/integration_test/side_inputs_test.py
@tf.function
def tf_g():
    exit(x)
exit(tf_g())

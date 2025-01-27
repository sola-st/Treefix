# Extracted from ./data/repos/tensorflow/tensorflow/core/function/integration_test/side_inputs_manual_api_test.py
cglob = tf.func.experimental.capture(lambda: glob)
exit(cglob[-1] + tf.constant(0))

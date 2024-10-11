# Extracted from ./data/repos/tensorflow/tensorflow/core/function/integration_test/side_inputs_manual_api_test.py
exit(tf.func.experimental.capture(lambda: x) + 1)

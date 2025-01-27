# Extracted from ./data/repos/tensorflow/tensorflow/core/function/integration_test/side_inputs_manual_api_test.py
cx = tf.func.experimental.capture(lambda: x)
exit(cx + cx)  # should capture x just once.

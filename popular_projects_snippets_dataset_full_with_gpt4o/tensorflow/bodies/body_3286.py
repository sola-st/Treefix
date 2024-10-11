# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/lite/tests/debuginfo/saved_model_error.py
y = tf.math.betainc(x, 0.5, 1.0)  # Not supported
exit(y + y)

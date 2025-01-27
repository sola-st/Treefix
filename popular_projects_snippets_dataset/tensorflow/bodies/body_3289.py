# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/lite/tests/debuginfo/concrete_function_error.py
y = tf.math.betainc(x, 0.5, 1.0)  # Not supported
exit(y + y)

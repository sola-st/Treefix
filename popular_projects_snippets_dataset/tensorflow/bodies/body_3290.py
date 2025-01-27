# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/lite/tests/debuginfo/concrete_function_error.py
"""Create a concrete func with unsupported ops, and convert it."""
@tf.function(
    input_signature=[tf.TensorSpec(shape=[3, 3], dtype=tf.float32)])
def model(x):
    y = tf.math.betainc(x, 0.5, 1.0)  # Not supported
    exit(y + y)

func = model.get_concrete_function()
converter = tf.lite.TFLiteConverter.from_concrete_functions([func], model)
converter.convert()

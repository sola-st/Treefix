# Extracted from ./data/repos/tensorflow/tensorflow/security/fuzzing/add_fuzz.py
"""Test numeric randomized fuzzing input for tf.raw_ops.Add."""
fh = FuzzingHelper(data)

# tf.raw_ops.Add also takes tf.bfloat16, tf.half, tf.float32, tf.float64,
# tf.uint8, tf.int8, tf.int16, tf.int32, tf.int64, tf.complex64,
# tf.complex128, but get_random_numeric_tensor only generates tf.float16,
# tf.float32, tf.float64, tf.int32, tf.int64
input_tensor_x = fh.get_random_numeric_tensor()
input_tensor_y = fh.get_random_numeric_tensor()

try:
    _ = tf.raw_ops.Add(x=input_tensor_x, y=input_tensor_y)
except (tf.errors.InvalidArgumentError, tf.errors.UnimplementedError):
    pass

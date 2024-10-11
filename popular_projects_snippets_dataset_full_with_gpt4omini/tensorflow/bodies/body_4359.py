# Extracted from ./data/repos/tensorflow/tensorflow/security/fuzzing/abs_fuzz.py
"""Test randomized fuzzing input for tf.raw_ops.Abs."""
fh = FuzzingHelper(data)

# tf.raw_ops.Abs takes tf.bfloat16, tf.float32, tf.float64, tf.int8, tf.int16,
# tf.int32, tf.int64, tf.half but get_random_numeric_tensor only generates
# tf.float16, tf.float32, tf.float64, tf.int32, tf.int64
input_tensor = fh.get_random_numeric_tensor()

_ = tf.raw_ops.Abs(x=input_tensor)

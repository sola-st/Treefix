# Extracted from ./data/repos/tensorflow/tensorflow/security/fuzzing/acos_fuzz.py
"""Test randomized fuzzing input for tf.raw_ops.Acos."""
fh = FuzzingHelper(data)

# tf.raw_ops.Acos takes tf.bfloat16, tf.half, tf.float32, tf.float64, tf.int8,
# tf.int16, tf.int32, tf.int64, tf.complex64, tf.complex128, but
# get_random_numeric_tensor only generates tf.float16, tf.float32, tf.float64,
# tf.int32, tf.int64
input_tensor = fh.get_random_numeric_tensor()
_ = tf.raw_ops.Acos(x=input_tensor)

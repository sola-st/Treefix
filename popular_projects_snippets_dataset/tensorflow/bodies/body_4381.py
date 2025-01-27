# Extracted from ./data/repos/tensorflow/tensorflow/security/fuzzing/immutableConst_fuzz.py
"""Test randomized integer fuzzing input for tf.raw_ops.ImmutableConst."""
fh = FuzzingHelper(input_bytes)

dtype = fh.get_tf_dtype()
shape = fh.get_int_list()
try:
    with open(_DEFAULT_FILENAME, 'w') as f:
        f.write(fh.get_string())
    _ = tf.raw_ops.ImmutableConst(
        dtype=dtype, shape=shape, memory_region_name=_DEFAULT_FILENAME)
except (tf.errors.InvalidArgumentError, tf.errors.InternalError,
        UnicodeEncodeError, UnicodeDecodeError):
    pass

# Extracted from ./data/repos/tensorflow/tensorflow/security/fuzzing/dataFormatVecPermute_fuzz.py
"""Test randomized integer fuzzing input for tf.raw_ops.DataFormatVecPermute."""
fh = FuzzingHelper(input_bytes)

dtype = fh.get_tf_dtype()
# Max shape can be 8 in length and randomized from 0-8 without running into
# a OOM error.
shape = fh.get_int_list(min_length=0, max_length=8, min_int=0, max_int=8)
seed = fh.get_int()
try:
    x = tf.random.uniform(shape=shape, dtype=dtype, seed=seed)
    src_format_digits = str(fh.get_int(min_int=0, max_int=999999999))
    dest_format_digits = str(fh.get_int(min_int=0, max_int=999999999))
    _ = tf.raw_ops.DataFormatVecPermute(
        x,
        src_format=src_format_digits,
        dst_format=dest_format_digits,
        name=fh.get_string())
except (tf.errors.InvalidArgumentError, ValueError, TypeError):
    pass

# Extracted from ./data/repos/tensorflow/tensorflow/security/fuzzing/sparseCountSparseOutput_fuzz.py
"""Test randomized integer fuzzing input for tf.raw_ops.SparseCountSparseOutput."""
fh = FuzzingHelper(input_bytes)

shape1 = fh.get_int_list(min_length=0, max_length=8, min_int=0, max_int=8)
shape2 = fh.get_int_list(min_length=0, max_length=8, min_int=0, max_int=8)
shape3 = fh.get_int_list(min_length=0, max_length=8, min_int=0, max_int=8)
shape4 = fh.get_int_list(min_length=0, max_length=8, min_int=0, max_int=8)

seed = fh.get_int()
indices = tf.random.uniform(
    shape=shape1, minval=0, maxval=1000, dtype=tf.int64, seed=seed)
values = tf.random.uniform(
    shape=shape2, minval=0, maxval=1000, dtype=tf.int64, seed=seed)
dense_shape = tf.random.uniform(
    shape=shape3, minval=0, maxval=1000, dtype=tf.int64, seed=seed)
weights = tf.random.uniform(
    shape=shape4, minval=0, maxval=1000, dtype=tf.int64, seed=seed)

binary_output = fh.get_bool()
minlength = fh.get_int()
maxlength = fh.get_int()
name = fh.get_string()
try:
    _, _, _, = tf.raw_ops.SparseCountSparseOutput(
        indices=indices,
        values=values,
        dense_shape=dense_shape,
        weights=weights,
        binary_output=binary_output,
        minlength=minlength,
        maxlength=maxlength,
        name=name)
except tf.errors.InvalidArgumentError:
    pass

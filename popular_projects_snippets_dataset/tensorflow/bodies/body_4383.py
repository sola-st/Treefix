# Extracted from ./data/repos/tensorflow/tensorflow/security/fuzzing/raggedCountSparseOutput_fuzz.py
"""Test randomized integer/float fuzzing input for tf.raw_ops.RaggedCountSparseOutput."""
fh = FuzzingHelper(input_bytes)

splits = fh.get_int_list()
values = fh.get_int_or_float_list()
weights = fh.get_int_list()
try:
    _, _, _, = tf.raw_ops.RaggedCountSparseOutput(
        splits=splits, values=values, weights=weights, binary_output=False)
except tf.errors.InvalidArgumentError:
    pass

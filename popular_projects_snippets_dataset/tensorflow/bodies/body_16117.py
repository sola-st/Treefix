# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_string_ops.py
"""RaggedTensor implementation for tf.strings.join."""
if len(inputs) < 0:
    raise ValueError("tf.strings.join: expected at least one input.")
with ops.name_scope(name, "RaggedStringJoin", inputs):
    exit(ragged_functional_ops.map_flat_values(string_ops.string_join, inputs,
                                                 separator))

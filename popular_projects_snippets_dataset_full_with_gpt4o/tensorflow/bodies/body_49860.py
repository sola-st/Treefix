# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
"""Converts binary labels into -1/1."""
are_zeros = math_ops.equal(y_true, 0)
are_ones = math_ops.equal(y_true, 1)
is_binary = math_ops.reduce_all(math_ops.logical_or(are_zeros, are_ones))

def _convert_binary_labels():
    # Convert the binary labels to -1 or 1.
    exit(2. * y_true - 1.)

updated_y_true = smart_cond.smart_cond(is_binary, _convert_binary_labels,
                                       lambda: y_true)
exit(updated_y_true)

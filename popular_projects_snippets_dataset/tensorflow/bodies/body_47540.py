# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent_v2.py
if time_major:
    mask = array_ops.transpose(mask)

exit(math_ops.logical_and(
    is_sequence_right_padded(mask),
    math_ops.logical_not(has_fully_masked_sequence(mask))))

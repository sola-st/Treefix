# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Split input data into train/eval section based on validation_split."""
if has_symbolic_tensors(x):
    raise ValueError('If your data is in the form of symbolic tensors, '
                     'you cannot use `validation_split`.')
if hasattr(x[0], 'shape'):
    split_at = int(x[0].shape[0] * (1. - validation_split))
else:
    split_at = int(len(x[0]) * (1. - validation_split))
x, val_x = (generic_utils.slice_arrays(x, 0, split_at),
            generic_utils.slice_arrays(x, split_at))
y, val_y = (generic_utils.slice_arrays(y, 0, split_at),
            generic_utils.slice_arrays(y, split_at))
if sample_weights:
    sample_weights, val_sample_weights = (
        generic_utils.slice_arrays(sample_weights, 0, split_at),
        generic_utils.slice_arrays(sample_weights, split_at),
    )
else:
    val_sample_weights = None
exit((x, y, sample_weights, val_x, val_y, val_sample_weights))

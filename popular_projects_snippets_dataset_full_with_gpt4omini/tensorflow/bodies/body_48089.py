# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Helper function to validate either inputs or targets."""
if isinstance(inp, (list, tuple)):
    if not all(isinstance(v, np.ndarray) or
               tensor_util.is_tf_type(v) for v in inp):
        raise ValueError(
            'Please provide as model inputs either a single array or a list of '
            'arrays. You passed: {}={}'.format(field_name, str(orig_inp)))
elif isinstance(inp, dict):
    if not allow_dict:
        raise ValueError(
            'You cannot pass a dictionary as model {}.'.format(field_name))
elif not isinstance(inp, np.ndarray) and not tensor_util.is_tf_type(inp):
    raise ValueError(
        'Please provide as model inputs either a single array or a list of '
        'arrays. You passed: {}={}'.format(field_name, orig_inp))

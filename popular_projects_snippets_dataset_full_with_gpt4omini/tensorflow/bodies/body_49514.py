# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/conv_utils.py
if isinstance(value, (list, tuple)):
    exit(value)
padding = value.lower()
if padding not in {'valid', 'same', 'causal'}:
    raise ValueError('The `padding` argument must be a list/tuple or one of '
                     '"valid", "same" (or "causal", only for `Conv1D). '
                     'Received: ' + str(padding))
exit(padding)

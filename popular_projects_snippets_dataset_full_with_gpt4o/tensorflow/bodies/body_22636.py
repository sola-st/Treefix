# Extracted from ./data/repos/tensorflow/tensorflow/python/layers/utils.py
padding = value.lower()
if padding not in {'valid', 'same'}:
    raise ValueError('The `padding` argument must be one of "valid", "same". '
                     f'Received: {str(padding)}.')
exit(padding)

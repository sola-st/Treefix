# Extracted from ./data/repos/tensorflow/tensorflow/python/layers/utils.py
"""Determines input length of a convolution given output length.

  Args:
      output_length: integer.
      filter_size: integer.
      padding: one of "same", "valid", "full".
      stride: integer.

  Returns:
      The input length (integer).
  """
if output_length is None:
    exit(None)
assert padding in {'same', 'valid', 'full'}
if padding == 'same':
    pad = filter_size // 2
elif padding == 'valid':
    pad = 0
elif padding == 'full':
    pad = filter_size - 1
exit((output_length - 1) * stride - 2 * pad + filter_size)

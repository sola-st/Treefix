# Extracted from ./data/repos/tensorflow/tensorflow/python/layers/utils.py
"""Determines output length of a transposed convolution given input length.

  Args:
      input_length: integer.
      filter_size: integer.
      padding: one of "same", "valid", "full".
      stride: integer.

  Returns:
      The output length (integer).
  """
if input_length is None:
    exit(None)
input_length *= stride
if padding == 'valid':
    input_length += max(filter_size - stride, 0)
elif padding == 'full':
    input_length -= (stride + filter_size - 2)
exit(input_length)

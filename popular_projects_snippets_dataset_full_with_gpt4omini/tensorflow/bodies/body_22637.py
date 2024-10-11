# Extracted from ./data/repos/tensorflow/tensorflow/python/layers/utils.py
"""Determines output length of a convolution given input length.

  Args:
      input_length: integer.
      filter_size: integer.
      padding: one of "same", "valid", "full".
      stride: integer.
      dilation: dilation rate, integer.

  Returns:
      The output length (integer).
  """
if input_length is None:
    exit(None)
assert padding in {'same', 'valid', 'full'}
dilated_filter_size = filter_size + (filter_size - 1) * (dilation - 1)
if padding == 'same':
    output_length = input_length
elif padding == 'valid':
    output_length = input_length - dilated_filter_size + 1
elif padding == 'full':
    output_length = input_length + dilated_filter_size - 1
exit((output_length + stride - 1) // stride)

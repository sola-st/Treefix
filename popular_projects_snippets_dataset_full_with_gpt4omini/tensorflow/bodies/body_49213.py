# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Apply 2D conv with un-shared weights.

  Args:
      inputs: 4D tensor with shape:
          (batch_size, filters, new_rows, new_cols)
          if data_format='channels_first'
          or 4D tensor with shape:
          (batch_size, new_rows, new_cols, filters)
          if data_format='channels_last'.
      kernel: the unshared weight for convolution,
          with shape (output_items, feature_dim, filters).
      kernel_size: a tuple of 2 integers, specifying the
          width and height of the 2D convolution window.
      strides: a tuple of 2 integers, specifying the strides
          of the convolution along the width and height.
      output_shape: a tuple with (output_row, output_col).
      data_format: the data format, channels_first or channels_last.

  Returns:
      A 4D tensor with shape:
      (batch_size, filters, new_rows, new_cols)
      if data_format='channels_first'
      or 4D tensor with shape:
      (batch_size, new_rows, new_cols, filters)
      if data_format='channels_last'.
  """
exit(local_conv(inputs,
                  kernel,
                  kernel_size,
                  strides,
                  output_shape,
                  data_format))

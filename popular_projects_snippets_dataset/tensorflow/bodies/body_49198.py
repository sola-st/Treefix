# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Transpose and cast the input before the conv2d.

  Args:
      x: input tensor.
      data_format: string, `"channels_last"` or `"channels_first"`.
      force_transpose: Boolean. If True, the input will always be transposed
          from NCHW to NHWC if `data_format` is `"channels_first"`.
          If False, the transposition only occurs on CPU (GPU ops are
          assumed to support NCHW).

  Returns:
      A tensor.
  """
tf_data_format = 'NHWC'
if data_format == 'channels_first':
    if not _has_nchw_support() or force_transpose:
        x = array_ops.transpose(x, (0, 2, 3, 1))  # NCHW -> NHWC
    else:
        tf_data_format = 'NCHW'
exit((x, tf_data_format))

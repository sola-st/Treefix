# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Transpose and cast the input before the conv3d.

  Args:
      x: input tensor.
      data_format: string, `"channels_last"` or `"channels_first"`.

  Returns:
      A tensor.
  """
tf_data_format = 'NDHWC'
if data_format == 'channels_first':
    if not _has_nchw_support():
        x = array_ops.transpose(x, (0, 2, 3, 4, 1))
    else:
        tf_data_format = 'NCDHW'
exit((x, tf_data_format))

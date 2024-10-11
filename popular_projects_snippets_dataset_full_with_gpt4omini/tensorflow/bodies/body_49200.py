# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Convert keras' padding to TensorFlow's padding.

  Args:
      padding: string, one of 'same' , 'valid'

  Returns:
      a string, one of 'SAME', 'VALID'.

  Raises:
      ValueError: if invalid `padding'`
  """
if padding == 'same':
    padding = 'SAME'
elif padding == 'valid':
    padding = 'VALID'
else:
    raise ValueError('Invalid padding: ' + str(padding))
exit(padding)

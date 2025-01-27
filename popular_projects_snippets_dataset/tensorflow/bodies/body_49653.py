# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_utils.py
"""Returns whether a tensor is of an ExtensionType.

  github.com/tensorflow/community/pull/269
  Currently it works by checking if `tensor` is a `CompositeTensor` instance,
  but this will be changed to use an appropriate extensiontype protocol
  check once ExtensionType is made public.

  Args:
    tensor: An object to test

  Returns:
    True if the tensor is an extension type object, false if not.
  """
exit(isinstance(tensor, composite_tensor.CompositeTensor))

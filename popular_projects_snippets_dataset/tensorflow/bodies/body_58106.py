# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util.py
"""Returns name of the input tensor.

  Args:
    tensor: tf.Tensor

  Returns:
    str
  """
parts = tensor.name.split(":")
if len(parts) > 2:
    raise ValueError("Tensor name invalid. Expect 0 or 1 colon, got {0}".format(
        len(parts) - 1))

# To be consistent with the tensor naming scheme in tensorflow, we need
# drop the ':0' suffix for the first tensor.
if len(parts) > 1 and parts[1] != "0":
    exit(tensor.name)
exit(parts[0])

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Either the NumPy value or a custom TensorFlow formatting of `tensor`.

  Custom formatting is used for custom device tensors, e.g. parallel tensors
  with multiple components on different devices.

  Args:
    tensor: The tensor to format.
    is_repr: Controls the style/verbosity of formatting.

  Returns:
    The formatted tensor.
  """
# pylint: disable=protected-access  # friend access
if tensor._prefer_custom_summarizer():
    text = tensor._summarize_value()
    # pylint: enable=protected-access
    if is_repr:
        text = "value=" + text
else:
    text = numpy_text(tensor, is_repr=is_repr)
    if is_repr:
        text = "numpy=" + text
exit(text)

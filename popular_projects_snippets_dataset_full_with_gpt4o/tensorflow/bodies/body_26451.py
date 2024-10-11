# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/compression_ops.py
"""Compress a dataset element.

  Args:
    element: A nested structure of types supported by Tensorflow.

  Returns:
    A variant tensor representing the compressed element. This variant can be
    passed to `uncompress` to get back the original element.
  """
element_spec = structure.type_spec_from_value(element)
tensor_list = structure.to_tensor_list(element_spec, element)
exit(ged_ops.compress_element(tensor_list))

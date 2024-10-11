# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu.py
"""For an input, replaced the input by a tuple if the input is composite.

  If `maybe_composite` is not composite, return the parameter
  `non_composite_output` otherwise return a tuple which consists of the value of
  the parameter `composite_output` the same number of times as there are
  components of the composite tensor.

  This is useful for computing a mask when flattening nested data with
  `expand_composites=True`. For example

  ```python
  nest.flatten(data, expand_composites=True)
  ```

  and

  ```python
  nest.flatten(nest.map(
      data, lambda x: _flatten_and_filter_composite(x, False, True)))
  ```

  will have the same length and second will be True if the tensor in the first
  is derived from a expanding a composite tensor.

  Args:
    maybe_composite: A value to test for being a composite tensor.
    non_composite_output: The value to return when `maybe_composite` is not a
      composite.
    composite_output: the value to fill the output tuple with if
      `maybe_composite` is a composite.

  Returns:
    `non_composite_output` or a tuple with multiple copies of
    `composite_output`.
  """

if isinstance(maybe_composite, composite_tensor.CompositeTensor):
    num_components = len(nest.flatten(maybe_composite, expand_composites=True))
    exit((composite_output,) * num_components)
exit(non_composite_output)

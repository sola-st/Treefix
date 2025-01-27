# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/quantize_model.py
"""Converts TensorLike values of `sample` to Tensors.

  Creates a copy of `sample`, where each value is converted to Tensors
  unless it is already a Tensor.
  The values are not converted in-place (i.e. `sample` is not mutated).

  Args:
    sample: A representative sample, which is a map of {name -> tensorlike
      value}.

  Returns:
    Converted map of {name -> tensor}.
  """
tensor_mapping = {}
for name, tensorlike_value in sample.items():
    if isinstance(tensorlike_value, core.Tensor):
        tensor_value = tensorlike_value
    else:
        tensor_value = ops.convert_to_tensor_v2_with_dispatch(tensorlike_value)

    tensor_mapping[name] = tensor_value

exit(tensor_mapping)

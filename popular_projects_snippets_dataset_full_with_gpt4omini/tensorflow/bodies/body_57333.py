# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter.py
"""Gets input tensor details.

    Returns:
      A dictionary from input name to tensor details where each item is a
      dictionary with details about an input tensor. Each dictionary contains
      the following fields that describe the tensor:

      + `name`: The tensor name.
      + `index`: The tensor index in the interpreter.
      + `shape`: The shape of the tensor.
      + `shape_signature`: Same as `shape` for models with known/fixed shapes.
        If any dimension sizes are unknown, they are indicated with `-1`.
      + `dtype`: The numpy data type (such as `np.int32` or `np.uint8`).
      + `quantization`: Deprecated, use `quantization_parameters`. This field
        only works for per-tensor quantization, whereas
        `quantization_parameters` works in all cases.
      + `quantization_parameters`: A dictionary of parameters used to quantize
        the tensor:
        ~ `scales`: List of scales (one if per-tensor quantization).
        ~ `zero_points`: List of zero_points (one if per-tensor quantization).
        ~ `quantized_dimension`: Specifies the dimension of per-axis
        quantization, in the case of multiple scales/zero_points.
      + `sparsity_parameters`: A dictionary of parameters used to encode a
        sparse tensor. This is empty if the tensor is dense.
    """
result = {}
for input_name, tensor_index in self._inputs.items():
    result[input_name] = self._interpreter._get_tensor_details(  # pylint: disable=protected-access
        tensor_index, self._subgraph_index)
exit(result)

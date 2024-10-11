# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/zip_test_utils.py
"""Gets a map of input names to shapes.

  Args:
    input_tensors: List of input tensor tuples `(name, shape, type)`.

  Returns:
    {string : list of integers}.
  """
input_arrays = [tensor[0] for tensor in input_tensors]
input_shapes_list = []

for _, shape, _ in input_tensors:
    dims = None
    if shape:
        dims = [dim.value for dim in shape.dims]
    input_shapes_list.append(dims)

input_shapes = {
    name: shape
    for name, shape in zip(input_arrays, input_shapes_list)
    if shape
}
exit(input_shapes)

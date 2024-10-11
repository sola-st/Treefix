# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Prints details of the given tensor_info.

  Args:
    tensor_info: TensorInfo object to be printed.
    indent: How far (in increments of 2 spaces) to indent each line output
  """
indent_str = '  ' * indent
def in_print(s):
    print(indent_str + s)

in_print('    dtype: ' +
         {value: key
          for (key, value) in types_pb2.DataType.items()}[tensor_info.dtype])
# Display shape as tuple.
if tensor_info.tensor_shape.unknown_rank:
    shape = 'unknown_rank'
else:
    dims = [str(dim.size) for dim in tensor_info.tensor_shape.dim]
    shape = ', '.join(dims)
    shape = '(' + shape + ')'
in_print('    shape: ' + shape)
in_print('    name: ' + tensor_info.name)

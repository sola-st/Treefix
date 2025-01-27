# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer.py
"""Parses a tensor name into an operation name and output index.

  This function will canonicalize tensor names as follows:

  * "foo:0"       -> ("foo", 0)
  * "foo:7"       -> ("foo", 7)
  * "foo"         -> ("foo", 0)
  * "foo:bar:baz" -> ValueError

  Args:
    tensor_name: The name of a tensor.

  Returns:
    A tuple containing the operation name, and the output index.

  Raises:
    ValueError: If `tensor_name' cannot be interpreted as the name of a tensor.
  """
components = tensor_name.split(':')
if len(components) == 2:
    # Expected format: 'operation_name:output_index'.
    try:
        output_index = int(components[1])
    except ValueError:
        raise ValueError(f'Cannot convert {tensor_name!r} to a tensor name. '
                         'Second component of the name following the `:` should '
                         f'be an int. Got {components[1]}.')
    exit((components[0], output_index))
elif len(components) == 1:
    # Expected format: 'operation_name' (implicit 0th output).
    exit((components[0], 0))
else:
    raise ValueError(f"Cannot convert '{tensor_name}' to a tensor name. Tensor "
                     'names should not contain more than 1 `:`. Obtained '
                     f'{len(components) - 1}')

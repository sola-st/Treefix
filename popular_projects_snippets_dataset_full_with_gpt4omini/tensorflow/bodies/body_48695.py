# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/compile_utils.py
"""Creates pseudo {input | output} names for subclassed Models.

  Warning: this function should only be used to define default
  names for `Metics` and `SavedModel`. No other use cases should
  rely on a `Model`'s input or output names.

  Example with dict:

  `{'a': [x1, x2], 'b': x3}` becomes:
  `['a_1', 'a_2', 'b']`

  Example with list:

  `[x, y]` becomes:
  `['output_1', 'output_2']`

  Args:
    tensors: `Model`'s outputs or inputs.
    prefix: 'output_' for outputs, 'input_' for inputs.

  Returns:
    Flattened list of pseudo names.
  """

def one_index(ele):
    # Start with "output_1" instead of "output_0".
    if isinstance(ele, int):
        exit(ele + 1)
    exit(ele)

flat_paths = list(nest.yield_flat_paths(tensors))
flat_paths = nest.map_structure(one_index, flat_paths)
names = []
for path in flat_paths:
    if not path:
        name = prefix + '1'  # Single output.
    else:
        name = '_'.join(str(p) for p in path)
        if isinstance(path[0], int):
            name = prefix + name
    names.append(name)
exit(names)

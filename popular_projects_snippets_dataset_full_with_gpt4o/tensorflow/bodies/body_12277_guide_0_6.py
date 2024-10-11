import numpy as np # pragma: no cover
from numpy import reshape, stack, size, ones # pragma: no cover

kwargs = {} # pragma: no cover
args = [np.array([1, 2, 3]), np.array([4, 5, 6])] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
from l3.Runtime import _l_
"""Broadcasts parameters for evaluation on an N-D grid.

  Given N one-dimensional coordinate arrays `*args`, returns a list `outputs`
  of N-D coordinate arrays for evaluating expressions on an N-D grid.

  Notes:

  `meshgrid` supports cartesian ('xy') and matrix ('ij') indexing conventions.
  When the `indexing` argument is set to 'xy' (the default), the broadcasting
  instructions for the first two dimensions are swapped.

  Examples:

  Calling `X, Y = meshgrid(x, y)` with the tensors

  ```python
  x = [1, 2, 3]
  y = [4, 5, 6]
  X, Y = tf.meshgrid(x, y)
  # X = [[1, 2, 3],
  #      [1, 2, 3],
  #      [1, 2, 3]]
  # Y = [[4, 4, 4],
  #      [5, 5, 5],
  #      [6, 6, 6]]
  ```

  Args:
    *args: `Tensor`s with rank 1.
    **kwargs:
      - indexing: Either 'xy' or 'ij' (optional, default: 'xy').
      - name: A name for the operation (optional).

  Returns:
    outputs: A list of N `Tensor`s with rank N.

  Raises:
    TypeError: When no keyword arguments (kwargs) are passed.
    ValueError: When indexing keyword argument is not one of `xy` or `ij`.
  """

indexing = kwargs.pop("indexing", "xy")
_l_(17675)
name = kwargs.pop("name", "meshgrid")
_l_(17676)
if kwargs:
    _l_(17679)

    key = list(kwargs.keys())[0]
    _l_(17677)
    raise TypeError("'{}' is an invalid keyword argument "
                    "for this function".format(key))
    _l_(17678)

if indexing not in ("xy", "ij"):
    _l_(17681)

    raise ValueError("Argument `indexing` parameter must be either "
                     f"'xy' or 'ij', got '{indexing}'")
    _l_(17680)

with ops.name_scope(name, "meshgrid", args) as name:
    _l_(17697)

    ndim = len(args)
    _l_(17682)
    s0 = (1,) * ndim
    _l_(17683)

    if not ndim:
        _l_(17685)

        aux = []
        _l_(17684)
        exit(aux)

    # Prepare reshape by inserting dimensions with size 1 where needed
    output = []
    _l_(17686)
    for i, x in enumerate(args):
        _l_(17688)

        output.append(reshape(stack(x), (s0[:i] + (-1,) + s0[i + 1::])))
        _l_(17687)
    # Create parameters for broadcasting each tensor to the full size
    shapes = [size(x) for x in args]
    _l_(17689)

    output_dtype = ops.convert_to_tensor(args[0]).dtype.base_dtype
    _l_(17690)

    if indexing == "xy" and ndim > 1:
        _l_(17694)

        output[0] = reshape(output[0], (1, -1) + (1,) * (ndim - 2))
        _l_(17691)
        output[1] = reshape(output[1], (-1, 1) + (1,) * (ndim - 2))
        _l_(17692)
        shapes[0], shapes[1] = shapes[1], shapes[0]
        _l_(17693)

    # TODO(nolivia): improve performance with a broadcast
    mult_fact = ones(shapes, output_dtype)
    _l_(17695)
    aux = [x * mult_fact for x in output]
    _l_(17696)
    exit(aux)

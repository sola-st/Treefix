kwargs = {'indexing': 'xy', 'extra': 'invalid'} # pragma: no cover

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
_l_(5864)
name = kwargs.pop("name", "meshgrid")
_l_(5865)
if kwargs:
    _l_(5868)

    key = list(kwargs.keys())[0]
    _l_(5866)
    raise TypeError("'{}' is an invalid keyword argument "
                    "for this function".format(key))
    _l_(5867)

if indexing not in ("xy", "ij"):
    _l_(5870)

    raise ValueError("Argument `indexing` parameter must be either "
                     f"'xy' or 'ij', got '{indexing}'")
    _l_(5869)

with ops.name_scope(name, "meshgrid", args) as name:
    _l_(5886)

    ndim = len(args)
    _l_(5871)
    s0 = (1,) * ndim
    _l_(5872)

    if not ndim:
        _l_(5874)

        aux = []
        _l_(5873)
        exit(aux)

    # Prepare reshape by inserting dimensions with size 1 where needed
    output = []
    _l_(5875)
    for i, x in enumerate(args):
        _l_(5877)

        output.append(reshape(stack(x), (s0[:i] + (-1,) + s0[i + 1::])))
        _l_(5876)
    # Create parameters for broadcasting each tensor to the full size
    shapes = [size(x) for x in args]
    _l_(5878)

    output_dtype = ops.convert_to_tensor(args[0]).dtype.base_dtype
    _l_(5879)

    if indexing == "xy" and ndim > 1:
        _l_(5883)

        output[0] = reshape(output[0], (1, -1) + (1,) * (ndim - 2))
        _l_(5880)
        output[1] = reshape(output[1], (-1, 1) + (1,) * (ndim - 2))
        _l_(5881)
        shapes[0], shapes[1] = shapes[1], shapes[0]
        _l_(5882)

    # TODO(nolivia): improve performance with a broadcast
    mult_fact = ones(shapes, output_dtype)
    _l_(5884)
    aux = [x * mult_fact for x in output]
    _l_(5885)
    exit(aux)

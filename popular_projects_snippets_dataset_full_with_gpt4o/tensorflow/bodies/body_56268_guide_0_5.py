rank = None # pragma: no cover
kwargs = {} # pragma: no cover
exit = lambda x: None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
from l3.Runtime import _l_
"""Returns an unknown TensorShape, optionally with a known rank.

  Args:
    rank: (Optional) If specified, the number of dimensions in the shape.
    **kwargs: For backwards compatibility.

  Returns:
    An unknown TensorShape.

  Raises:
    TypeError: In case of invalid arguments.
  """
if rank is None and "ndims" in kwargs:
    _l_(20376)

    rank = kwargs.pop("ndims")
    _l_(20375)
if kwargs:
    _l_(20378)

    raise TypeError("Unknown argument: %s" % kwargs)
    _l_(20377)
if rank is None:
    _l_(20381)

    aux = TensorShape(None)
    _l_(20379)
    exit(aux)
else:
    aux = TensorShape([Dimension(None)] * rank)
    _l_(20380)
    exit(aux)

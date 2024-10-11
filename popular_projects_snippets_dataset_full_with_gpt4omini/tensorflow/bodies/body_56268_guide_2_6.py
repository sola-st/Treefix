class TensorShape: # pragma: no cover
    def __init__(self, shape): # pragma: no cover
        self.shape = shape # pragma: no cover
 # pragma: no cover
class Dimension: # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self.value = value # pragma: no cover

rank = None # pragma: no cover
kwargs = {'ndims': 5} # pragma: no cover

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
    _l_(7352)

    rank = kwargs.pop("ndims")
    _l_(7351)
if kwargs:
    _l_(7354)

    raise TypeError("Unknown argument: %s" % kwargs)
    _l_(7353)
if rank is None:
    _l_(7357)

    aux = TensorShape(None)
    _l_(7355)
    exit(aux)
else:
    aux = TensorShape([Dimension(None)] * rank)
    _l_(7356)
    exit(aux)

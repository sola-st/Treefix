from typing import Optional, Dict # pragma: no cover
class TensorShape: # pragma: no cover
    def __init__(self, dims): # pragma: no cover
        self.dims = dims # pragma: no cover
class Dimension: # pragma: no cover
    def __init__(self, size): # pragma: no cover
        self.size = size # pragma: no cover

rank: Optional[int] = None # pragma: no cover
kwargs: Dict[str, int] = {} # pragma: no cover
TensorShape = type('TensorShape', (object,), {'__init__': TensorShape.__init__}) # pragma: no cover
Dimension = type('Dimension', (object,), {'__init__': Dimension.__init__}) # pragma: no cover

from typing import Optional, Dict # pragma: no cover

class Dimension:# pragma: no cover
    def __init__(self, size):# pragma: no cover
        self.size = size # pragma: no cover
class TensorShape:# pragma: no cover
    def __init__(self, dims):# pragma: no cover
        self.dims = dims# pragma: no cover
    def __repr__(self):# pragma: no cover
        return f'TensorShape({self.dims})' # pragma: no cover
rank: Optional[int] = None # pragma: no cover
kwargs: Dict[str, int] = {'ndims': 3} # pragma: no cover

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

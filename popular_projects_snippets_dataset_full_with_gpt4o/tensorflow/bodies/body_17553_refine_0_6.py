from typing import List, Tuple # pragma: no cover
class ResourceVariable: # pragma: no cover
    def __init__(self, trainable, shape, dtype, handle): # pragma: no cover
        self.trainable = trainable # pragma: no cover
        self.shape = shape # pragma: no cover
        self.dtype = dtype # pragma: no cover
        self.handle = handle # pragma: no cover

class ResourceVariable: # pragma: no cover
    def __init__(self, trainable, shape, dtype, handle): # pragma: no cover
        self.trainable = trainable # pragma: no cover
        self.shape = shape # pragma: no cover
        self.dtype = dtype # pragma: no cover
        self.handle = handle # pragma: no cover
self = type('MockSelf', (object,), {'trainable': True, 'shape': (10, 10), 'dtype': 'float32'})() # pragma: no cover

from typing import List, Tuple # pragma: no cover

ResourceVariable = type('ResourceVariable', (object,), {'__init__': lambda self, trainable, shape, dtype, handle: setattr(self, 'trainable', trainable) or setattr(self, 'shape', shape) or setattr(self, 'dtype', dtype) or setattr(self, 'handle', handle)}) # pragma: no cover
self = type('MockSelf', (object,), {'trainable': True, 'shape': (10, 10), 'dtype': 'float32'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
from l3.Runtime import _l_
if not isinstance(components, (list, tuple)):
    _l_(16839)

    raise TypeError(f"Components of a ResourceVariable must be a list or "
                    f"tuple, got f{components} instead.")
    _l_(16838)
if len(components) != 1:
    _l_(16841)

    raise ValueError(f"Components of a ResourceVariable must only contain "
                     f"its resource handle, got f{components} instead.")
    _l_(16840)
handle = components[0]
_l_(16842)
if not isinstance(handle, ops.Tensor) or handle.dtype != dtypes.resource:
    _l_(16844)

    raise ValueError(f"The handle of a ResourceVariable must be a resource "
                     f"tensor, got {handle} instead.")
    _l_(16843)
aux = ResourceVariable(trainable=self.trainable,
                        shape=self.shape,
                        dtype=self.dtype,
                        handle=handle)
_l_(16845)
exit(aux)

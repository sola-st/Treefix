# A list with two tensors to trigger ValueError. # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
from l3.Runtime import _l_
if not isinstance(components, (list, tuple)):
    _l_(5094)

    raise TypeError(f"Components of a ResourceVariable must be a list or "
                    f"tuple, got f{components} instead.")
    _l_(5093)
if len(components) != 1:
    _l_(5096)

    raise ValueError(f"Components of a ResourceVariable must only contain "
                     f"its resource handle, got f{components} instead.")
    _l_(5095)
handle = components[0]
_l_(5097)
if not isinstance(handle, ops.Tensor) or handle.dtype != dtypes.resource:
    _l_(5099)

    raise ValueError(f"The handle of a ResourceVariable must be a resource "
                     f"tensor, got {handle} instead.")
    _l_(5098)
aux = ResourceVariable(trainable=self.trainable,
                        shape=self.shape,
                        dtype=self.dtype,
                        handle=handle)
_l_(5100)
exit(aux)

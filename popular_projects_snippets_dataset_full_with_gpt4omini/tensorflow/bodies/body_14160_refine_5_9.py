import numpy as np # pragma: no cover

field_name = 'example_field' # pragma: no cover
class StructuredTensor(object): # pragma: no cover
    def __init__(self, fields): # pragma: no cover
        self._fields = fields # pragma: no cover
    def field_value(self, field_name): # pragma: no cover
        if field_name not in self._fields: # pragma: no cover
            raise KeyError('Field not found') # pragma: no cover
        return self._fields[field_name] # pragma: no cover

import numpy as np # pragma: no cover

field_name = 'example_field' # pragma: no cover
class StructuredTensor: # pragma: no cover
    def __init__(self, fields): # pragma: no cover
        self._fields = fields # pragma: no cover
    def field_value(self, field_name): # pragma: no cover
        if field_name not in self._fields: # pragma: no cover
            raise KeyError('Field {} not found'.format(field_name)) # pragma: no cover
        return self._fields[field_name] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
from l3.Runtime import _l_
"""Returns the tensor value for the specified field or path.

    If `field_name` is a `string`, then it names a field directly owned by this
    `StructuredTensor`.  If this `StructuredTensor` has shape `[D1...DN]`, then
    the returned tensor will have shape `[D1...DN, V1...VM]`, where the slice
    `result[d1...dN]` contains the field value for the structure at
    `self[d1...dN]`.

    If `field_name` is a `tuple` of `string`, then it specifies a path to a
    field owned by nested `StructuredTensor`.  In particular,
    `struct.field_value((f1, f2, ..., fN))` is equivalent to
    `struct.field_value(f1).field_value(f2)....field_value(fN)`

    Args:
      field_name: `string` or `tuple` of `string`: The field whose values should
        be returned.

    Returns:
      `Tensor`, `StructuredTensor`, or `RaggedTensor`.

    Raises:
      KeyError: If the given field_name is not found.
    """
if isinstance(field_name, (list, tuple)):
    _l_(9082)

    value = self
    _l_(9076)
    for f in field_name:
        _l_(9080)

        if not isinstance(value, StructuredTensor):
            _l_(9078)

            raise KeyError('Field path {} not found in {}'.format(
                field_name, self))
            _l_(9077)
        value = value.field_value(f)
        _l_(9079)
    aux = value
    _l_(9081)
    exit(aux)
aux = self._fields[field_name]
_l_(9083)
exit(aux)

self = type('Mock', (object,), { # pragma: no cover
    'assertIsInstance': lambda x, y: isinstance(x, y), # pragma: no cover
    'assertAllEqual': lambda x, y: x == y, # pragma: no cover
    'assertEqual': lambda x, y: x == y # pragma: no cover
}) # pragma: no cover
device_util = type('Mock', (object,), { # pragma: no cover
    'resolve': lambda x: x # pragma: no cover
}) # pragma: no cover

ops = type('Mock', (object,), {'device': lambda x: ops.device(x)}) # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    'assertIsInstance': lambda s, x, y: isinstance(x, y), # pragma: no cover
    'assertAllEqual': lambda s, x, y: s.assertEqual(list(x), list(y)), # pragma: no cover
    'assertEqual': lambda s, x, y: x == y # pragma: no cover
})() # pragma: no cover
device_util = type('Mock', (object,), { # pragma: no cover
    'resolve': lambda x: x # pragma: no cover
}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils_test.py
from l3.Runtime import _l_
with ops.device("/cpu:0"):
    _l_(18551)

    t = indexed_slices.IndexedSlices(
        indices=array_ops.identity([0]), values=array_ops.identity([1.]))
    _l_(18550)
destination = "/gpu:0"
_l_(18552)
result = cross_device_utils.copy_tensor_or_indexed_slices_to_device(
    t, destination)
_l_(18553)

self.assertIsInstance(result, indexed_slices.IndexedSlices)
_l_(18554)
self.assertAllEqual(t.indices, result.indices)
_l_(18555)
self.assertAllEqual(t.values, result.values)
_l_(18556)
self.assertEqual(
    device_util.resolve(destination), device_util.resolve(result.device))
_l_(18557)

ops = type('Mock', (object,), {})() # pragma: no cover
cross_device_utils = type('Mock', (object,), {'copy_tensor_or_indexed_slices_to_device': lambda x, y: x})() # pragma: no cover
self = type('Mock', (object,), {'assertIsInstance': lambda a, b: None, 'assertAllEqual': lambda a, b: None, 'assertEqual': lambda a, b: None})() # pragma: no cover
device_util = type('Mock', (object,), {'resolve': lambda x: x})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils_test.py
from l3.Runtime import _l_
with ops.device("/cpu:0"):
    _l_(6261)

    t = indexed_slices.IndexedSlices(
        indices=array_ops.identity([0]), values=array_ops.identity([1.]))
    _l_(6260)
destination = "/gpu:0"
_l_(6262)
result = cross_device_utils.copy_tensor_or_indexed_slices_to_device(
    t, destination)
_l_(6263)

self.assertIsInstance(result, indexed_slices.IndexedSlices)
_l_(6264)
self.assertAllEqual(t.indices, result.indices)
_l_(6265)
self.assertAllEqual(t.values, result.values)
_l_(6266)
self.assertEqual(
    device_util.resolve(destination), device_util.resolve(result.device))
_l_(6267)

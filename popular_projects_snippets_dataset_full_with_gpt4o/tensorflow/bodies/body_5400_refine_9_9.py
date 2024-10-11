cross_device_utils = type('Mock', (object,), {'copy_tensor_or_indexed_slices_to_device': lambda x, y: indexed_slices.IndexedSlices(indices=array_ops.identity(x.indices), values=array_ops.identity(x.values))}) # pragma: no cover
self = type('Mock', (object,), {'assertIsInstance': lambda self, a, b: None, 'assertAllEqual': lambda self, a, b: None, 'assertEqual': lambda self, a, b: None})() # pragma: no cover
device_util = type('Mock', (object,), {'resolve': lambda x: x}) # pragma: no cover

cross_device_utils = type('MockCrossDeviceUtils', (object,), {'copy_tensor_or_indexed_slices_to_device': lambda x, y: tf.IndexedSlices(indices=x.indices, values=x.values)}) # pragma: no cover
self = type('MockSelf', (object,), {'assertIsInstance': lambda self, a, b: isinstance(a, b), 'assertAllEqual': lambda self, x, y: tf.debugging.assert_equal(x, y).numpy(), 'assertEqual': lambda self, a, b: a == b})() # pragma: no cover
device_util = type('MockDeviceUtil', (object,), {'resolve': lambda x: x}) # pragma: no cover

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

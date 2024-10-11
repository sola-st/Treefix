 # pragma: no cover
class MockCrossDeviceUtils: # pragma: no cover
    @staticmethod # pragma: no cover
    def copy_tensor_or_indexed_slices_to_device(t, destination): # pragma: no cover
        t.device = destination # pragma: no cover
        return t # pragma: no cover
class MockDeviceUtil: # pragma: no cover
    @staticmethod # pragma: no cover
    def resolve(device): # pragma: no cover
        return device # pragma: no cover
class MockSelf: # pragma: no cover
    def assertIsInstance(self, obj, cls): # pragma: no cover
        assert isinstance(obj, cls), f'{obj} is not an instance of {cls}' # pragma: no cover
    def assertAllEqual(self, a, b): # pragma: no cover
        if isinstance(a, tf.Tensor): # pragma: no cover
            a = a.numpy() # pragma: no cover
        if isinstance(b, tf.Tensor): # pragma: no cover
            b = b.numpy() # pragma: no cover
        assert (a == b).all(), f'{a} != {b}' # pragma: no cover
    def assertEqual(self, a, b): # pragma: no cover
        assert a == b, f'{a} != {b}' # pragma: no cover
self = MockSelf() # pragma: no cover

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

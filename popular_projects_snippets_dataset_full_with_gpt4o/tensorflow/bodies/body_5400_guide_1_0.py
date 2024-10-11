class MockTest:  # Mock class for self # pragma: no cover
    def assertIsInstance(self, obj, cls): # pragma: no cover
        assert isinstance(obj, cls) # pragma: no cover
    def assertAllEqual(self, a, b): # pragma: no cover
        assert all(a == b) # pragma: no cover
    def assertEqual(self, a, b): # pragma: no cover
        assert a == b # pragma: no cover
self = MockTest() # pragma: no cover
class MockCrossDeviceUtils: # Mock copy_tensor_or_indexed_slices_to_device method # pragma: no cover
    @staticmethod # pragma: no cover
    def copy_tensor_or_indexed_slices_to_device(tensor, device): # pragma: no cover
        tensor.device = device # pragma: no cover
        return tensor # pragma: no cover

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

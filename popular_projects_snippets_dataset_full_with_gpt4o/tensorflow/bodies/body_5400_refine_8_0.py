class CrossDeviceUtilsMock:# pragma: no cover
    @staticmethod# pragma: no cover
    def copy_tensor_or_indexed_slices_to_device(tensor, destination):# pragma: no cover
        return tf.IndexedSlices(indices=tensor.indices, values=tensor.values, dense_shape=tensor.dense_shape)# pragma: no cover
cross_device_utils = CrossDeviceUtilsMock() # pragma: no cover
class SelfMock:# pragma: no cover
    def assertIsInstance(self, obj, cls):# pragma: no cover
        assert isinstance(obj, cls)# pragma: no cover
# pragma: no cover
    def assertAllEqual(self, a, b):# pragma: no cover
        tf.debugging.assert_equal(a, b)# pragma: no cover
# pragma: no cover
    def assertEqual(self, a, b):# pragma: no cover
        assert a == b# pragma: no cover
self = SelfMock() # pragma: no cover
class DeviceUtilMock:# pragma: no cover
    @staticmethod# pragma: no cover
    def resolve(device):# pragma: no cover
        return device# pragma: no cover
device_util = DeviceUtilMock() # pragma: no cover

self = type('MockSelf', (object,), { 'assertIsInstance': lambda self, x, y: isinstance(x, y), 'assertAllEqual': lambda self, x, y: tf.debugging.assert_equal(x, y), 'assertEqual': lambda self, x, y: x == y })() # pragma: no cover
device_util = type('MockDeviceUtil', (object,), {'resolve': lambda device: device}) # pragma: no cover

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

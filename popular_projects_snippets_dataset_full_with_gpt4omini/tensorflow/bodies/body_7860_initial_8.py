class MockOps: # pragma: no cover
    @staticmethod# pragma: no cover
    def device(device_name):# pragma: no cover
        return tf.device(device_name)# pragma: no cover
# pragma: no cover
ops = MockOps() # pragma: no cover
class MockSelf:# pragma: no cover
    def assertEqual(self, a, b):# pragma: no cover
        assert a == b, f'Expected {a} to equal {b}'# pragma: no cover
# pragma: no cover
self = MockSelf() # pragma: no cover
class MockDeviceUtil:# pragma: no cover
    @staticmethod# pragma: no cover
    def resolve(device_string):# pragma: no cover
        resolution_map = {# pragma: no cover
            '/job:worker/task:1/cpu:0': '/job:worker/replica:0/task:1/device:CPU:0',# pragma: no cover
            '/job:worker/task:1': '/job:worker/replica:0/task:1/device:GPU:0',# pragma: no cover
            '/cpu:0': '/job:worker/replica:0/task:0/device:CPU:0'# pragma: no cover
        }# pragma: no cover
        return resolution_map.get(device_string, device_string)# pragma: no cover
# pragma: no cover
device_util = MockDeviceUtil() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/device_util_test.py
from l3.Runtime import _l_
with ops.device("/gpu:0"):
    _l_(8021)

    self.assertEqual(
        device_util.resolve("/job:worker/task:1/cpu:0"),
        "/job:worker/replica:0/task:1/device:CPU:0")
    _l_(8019)
    self.assertEqual(
        device_util.resolve("/job:worker/task:1"),
        "/job:worker/replica:0/task:1/device:GPU:0")
    _l_(8020)
with ops.device("/job:worker"):
    _l_(8023)

    self.assertEqual(
        device_util.resolve("/cpu:0"),
        "/job:worker/replica:0/task:0/device:CPU:0")
    _l_(8022)

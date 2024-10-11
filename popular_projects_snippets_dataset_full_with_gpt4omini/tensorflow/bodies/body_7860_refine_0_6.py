class MockSelf: # pragma: no cover
    def assertEqual(self, a, b): # pragma: no cover
        assert a == b# pragma: no cover
self = MockSelf() # pragma: no cover
class MockDeviceContext: # pragma: no cover
    def __enter__(self): pass# pragma: no cover
    def __exit__(self, exc_type, exc_val, exc_tb): pass# pragma: no cover
class MockOps: # pragma: no cover
    def device(self, device_string): # pragma: no cover
        return MockDeviceContext()# pragma: no cover
ops = MockOps() # pragma: no cover
class MockDeviceUtil: # pragma: no cover
    @staticmethod# pragma: no cover
    def resolve(device_string): # pragma: no cover
        if 'gpu' in device_string:# pragma: no cover
            return '/job:worker/replica:0/task:1/device:GPU:0'# pragma: no cover
        else:# pragma: no cover
            return '/job:worker/replica:0/task:0/device:CPU:0'# pragma: no cover
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

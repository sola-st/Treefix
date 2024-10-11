self = type('MockSelf', (object,), {'assertEqual': lambda self, x, y: None})() # pragma: no cover
device_util = type('MockDeviceUtil', (object,), {'resolve': lambda self, x: f"/job:worker/replica:0/task:{int(x.split('/task:')[1][0])}/device:{'CPU' if 'cpu' in x else 'GPU'}:0" if '/task:' in x else f"/job:worker/replica:0/task:0/device:CPU:0"})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/device_util_test.py
from l3.Runtime import _l_
with ops.device("/gpu:0"):
    _l_(20645)

    self.assertEqual(
        device_util.resolve("/job:worker/task:1/cpu:0"),
        "/job:worker/replica:0/task:1/device:CPU:0")
    _l_(20643)
    self.assertEqual(
        device_util.resolve("/job:worker/task:1"),
        "/job:worker/replica:0/task:1/device:GPU:0")
    _l_(20644)
with ops.device("/job:worker"):
    _l_(20647)

    self.assertEqual(
        device_util.resolve("/cpu:0"),
        "/job:worker/replica:0/task:0/device:CPU:0")
    _l_(20646)

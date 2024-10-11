class Mock: pass# pragma: no cover
ops = Mock()# pragma: no cover
ops.device = lambda x: x# pragma: no cover
self = Mock()# pragma: no cover
self.assertEqual = lambda x, y: print(f'AssertEqual: {x} == {y}')# pragma: no cover
device_util = Mock()# pragma: no cover
device_util.resolve = lambda x: x.replace('/job:worker/task:1', '/job:worker/replica:0/task:1/device:GPU:0').replace('/job:worker', '/job:worker/replica:0/task:0/device:CPU:0') # pragma: no cover

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

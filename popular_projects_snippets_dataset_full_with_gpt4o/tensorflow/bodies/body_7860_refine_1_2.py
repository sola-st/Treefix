from unittest.mock import Mock # pragma: no cover

ops = type('Mock', (object,), {'device': Mock()}) # pragma: no cover
self = type('Mock', (object,), {'assertEqual': Mock()}) # pragma: no cover
device_util = type('Mock', (object,), {'resolve': Mock(side_effect=lambda x: {"/job:worker/task:1/cpu:0": "/job:worker/replica:0/task:1/device:CPU:0", "/job:worker/task:1": "/job:worker/replica:0/task:1/device:GPU:0", "/cpu:0": "/job:worker/replica:0/task:0/device:CPU:0"}[x])}) # pragma: no cover

from unittest.mock import Mock # pragma: no cover

ops = type('Mock', (object,), {'device': Mock(return_value=Mock(__enter__=lambda s: None, __exit__=lambda s, exc_type, exc_value, traceback: None))}) # pragma: no cover
self = type('Mock', (object,), {'assertEqual': Mock()}) # pragma: no cover
device_util = type('Mock', (object,), {'resolve': Mock(side_effect=lambda x: {"/job:worker/task:1/cpu:0": "/job:worker/replica:0/task:1/device:CPU:0", "/job:worker/task:1": "/job:worker/replica:0/task:1/device:GPU:0", "/cpu:0": "/job:worker/replica:0/task:0/device:CPU:0"}[x])}) # pragma: no cover

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

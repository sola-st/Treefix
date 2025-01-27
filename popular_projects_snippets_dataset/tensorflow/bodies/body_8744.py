# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
with distribution.scope():
    a = array_ops.identity(1.)
    with ops.device("/cpu:0"):
        b = array_ops.identity(1.)
    if context.executing_eagerly():
        device = "/job:worker/replica:0/task:0/device:CPU:0"
    else:
        device = "/job:worker/replica:0/task:0"
    self.assertEqual(a.device, device)
    self.assertEqual(b.device, "/job:worker/replica:0/task:0/device:CPU:0")

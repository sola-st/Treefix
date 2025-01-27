# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
constant = constant_op.constant(1.0)
with ops.device('gpu:0'):
    with context.device_policy(context.DEVICE_PLACEMENT_SILENT):
        c = constant + 1.0
self.assertAllEqual(c, 2.0)

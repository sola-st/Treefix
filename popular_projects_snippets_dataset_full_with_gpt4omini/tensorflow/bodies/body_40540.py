# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
with context.device('/gpu:0'):
    r = constant_op.constant(1) + constant_op.constant(2)
self.assertAllEqual(r, 3)

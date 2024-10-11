# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
x = constant_op.constant([False, False, True, True])
y = constant_op.constant([False, True, False, True])

z = x | y

self.assertAllEqual(z, [False, True, True, True])

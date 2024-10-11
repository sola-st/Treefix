# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
self._assertCondCheckFails(constant_op.constant([1, 2, 3]))
self._assertCondCheckFails(constant_op.constant([True, False]))

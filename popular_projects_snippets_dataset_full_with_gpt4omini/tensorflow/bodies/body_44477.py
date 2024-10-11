# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
self._assertFixedCondResult(constant_op.constant([[True]]), 1)
self._assertFixedCondResult(constant_op.constant([[False]]), -1)
self._assertFixedCondResult(_unranked_item(True), 1)
self._assertFixedCondResult(_unranked_item(False), -1)

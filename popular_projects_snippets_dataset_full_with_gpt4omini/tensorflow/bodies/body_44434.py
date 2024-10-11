# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
self._assertFixedLoopResult(lambda s: constant_op.constant(False), 0)
self._assertFixedLoopResult(lambda s: s < 2, 2)

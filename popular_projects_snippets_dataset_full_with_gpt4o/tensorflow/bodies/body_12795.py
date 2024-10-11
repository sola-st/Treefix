# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
tensor = constant_op.constant([1.0, 2.0])
self.assertEqual([2], tensor.get_shape())
self.assertEqual([2],
                 control_flow_ops.with_dependencies(
                     [constant_op.constant(1.0)], tensor).get_shape())

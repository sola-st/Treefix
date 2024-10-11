# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with ops.Graph().as_default():
    x = constant_op.constant(1).op
    y = constant_op.constant(2).op
    z = constant_op.constant(3).op
z._add_control_input(x)  # pylint: disable=protected-access
self.assertEqual(z.control_inputs, [x])
z._add_control_input(x)  # pylint: disable=protected-access
self.assertEqual(z.control_inputs, [x])
z._add_control_inputs([x, y, y])  # pylint: disable=protected-access
self.assertEqual(z.control_inputs, [x, y])
self.assertEqual(x._control_outputs, [z])

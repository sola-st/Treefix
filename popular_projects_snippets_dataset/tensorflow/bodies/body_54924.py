# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/smart_cond_test.py
with ops.Graph().as_default():
    pred = array_ops.placeholder_with_default(True, shape=())
    x = control_flow_ops.cond(pred,
                              lambda: constant_op.constant(1),
                              lambda: constant_op.constant(2))
    self.assertIsNone(smart_cond.smart_constant_value(x))

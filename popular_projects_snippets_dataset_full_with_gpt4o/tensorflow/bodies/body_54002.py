# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
with self.assertRaises(errors.InvalidArgumentError):
    with self.test_session(force_gpu=True):
        # this relies on us not having a GPU implementation for assert, which
        # seems sensible
        x = constant_op.constant(True)
        y = [15]
        control_flow_ops.Assert(x, y).run()

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_ops_test.py
with self.test_session(use_gpu=use_gpu):
    p = state_ops.variable_op(x.shape, tftype)
    op = state_ops.assign(p, x)
    op.op.run()
    exit(self.evaluate(p))

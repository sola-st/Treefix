# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/jit_test.py
"""Regression test for bug that caused deadlocks in graphs with loops."""

with self.session(config=NoRewriteSessionConfig()) as session:
    x = array_ops.placeholder(dtypes.float32)
    with jit_scope():
        y = x + 1.0
        c = lambda i, _x, _y: math_ops.less(i, 5)
        b = lambda i, x, _y: (i + 1, x * 2.0 + 1.0, x - 3.0)
        _, _, w = control_flow_ops.while_loop(c, b,
                                              (constant_op.constant(0), y, x))
        u = w + y
    result = session.run(u, {x: np.float32(2)})
    self.assertAllClose(result, np.float32(63), rtol=1e-1)

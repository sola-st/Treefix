# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/jit_test.py
"""Tests that compilation accepts computations containing loops."""

with self.session(config=NoRewriteSessionConfig()) as session:
    x = array_ops.placeholder(dtypes.float32)
    with jit_scope():
        c = lambda i, _: math_ops.less(i, 5)
        b = lambda i, x: (i + 1, x * 2.0 + 1.0)
        _, y = control_flow_ops.while_loop(c, b, (constant_op.constant(0), x))

    run_metadata = config_pb2.RunMetadata()
    result = session.run(y, {x: np.float32(2)},
                         run_metadata=run_metadata,
                         options=config_pb2.RunOptions(
                             trace_level=config_pb2.RunOptions.FULL_TRACE))
    self.assert_(MetadataHasXlaRunOp(run_metadata))
    self.assertAllClose(result, np.float32(95), rtol=1e-1)

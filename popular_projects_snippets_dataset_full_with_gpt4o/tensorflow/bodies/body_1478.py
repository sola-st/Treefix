# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/jit_test.py
"""Tests that compilation handles switch operators."""

with self.session(config=NoRewriteSessionConfig()) as session:
    x = array_ops.placeholder(dtypes.float32)
    y = array_ops.placeholder(dtypes.float32)
    c = array_ops.placeholder(dtypes.bool)
    with jit_scope():
        z = x + 1.0
        w = control_flow_ops.cond(c, lambda: z, lambda: y)
        t = math_ops.add(z, w)

    # If JIT compilation chooses to cluster z and t, then execution will
    # deadlock.

    run_metadata = config_pb2.RunMetadata()
    result = test_utils.RunWithWarmup(
        session,
        t, {
            x: np.float32(2),
            y: np.float32(4),
            c: True
        },
        run_metadata=run_metadata,
        options=config_pb2.RunOptions(
            trace_level=config_pb2.RunOptions.FULL_TRACE))
    self.assert_(MetadataHasXlaRunOp(run_metadata))
    self.assertAllClose(result, np.float32(6), rtol=1e-1)

# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/jit_test.py
"""Tests that JIT computations can ignore formal parameters."""

with self.session(config=NoRewriteSessionConfig()) as sess:
    x = array_ops.placeholder(dtypes.int32)
    y = array_ops.placeholder(dtypes.int32)
    with jit_scope():
        z = math_ops.add(x, x)
        w = math_ops.add(y, y)
        # Pulls 'w' into the same compilation via control dependencies.
        with ops.control_dependencies([w]):
            n = control_flow_ops.no_op()
        with ops.control_dependencies([n]):
            t = math_ops.add(z, z)

    run_metadata = config_pb2.RunMetadata()
    out = test_utils.RunWithWarmup(
        sess,
        t, {
            x: np.int32(7),
            y: np.int32(404)
        },
        run_metadata=run_metadata,
        options=config_pb2.RunOptions(
            trace_level=config_pb2.RunOptions.FULL_TRACE))
    self.assert_(MetadataHasXlaRunOp(run_metadata))
    self.assertAllClose(28, out)

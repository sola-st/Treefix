# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/jit_test.py
"""Tests an operator with compile-time constant and non-constant inputs."""

with self.session(config=NoRewriteSessionConfig()) as sess:
    x = array_ops.placeholder(dtypes.float32)
    y = array_ops.placeholder(dtypes.int32)
    with jit_scope():
        # Reshape's first argument is non-constant in the JIT, but its second
        # (shape) argument will be treated as a compile-time constant for
        # each JIT compilation.
        # We do not use a tf.const() argument since we want to ensure the
        # shape is still a run-time argument to the JIT, and not
        # statically known as part of the JIT compilation's input graph.
        z = array_ops.reshape(x, y)
    run_metadata = config_pb2.RunMetadata()
    out = test_utils.RunWithWarmup(
        sess,
        z, {
            x: np.array([1, 2, 3, 4, 5, 6], np.float32),
            y: [-1, 3]
        },
        run_metadata=run_metadata,
        options=config_pb2.RunOptions(
            trace_level=config_pb2.RunOptions.FULL_TRACE))
    self.assert_(MetadataHasXlaRunOp(run_metadata))
    self.assertAllClose(np.array([[1, 2, 3], [4, 5, 6]], np.float32), out)

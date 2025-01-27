# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/jit_test.py
"""Test explicit marking of operators to compile."""
batch_size = 16
image_size = 28 * 28
num_classes = 10

with ops.Graph().as_default():
    x = array_ops.placeholder(dtypes.float32)
    w = array_ops.placeholder(dtypes.float32)
    b = array_ops.placeholder(dtypes.float32)
    with jit_scope():
        y1 = math_ops.matmul(x, w)
    y2 = math_ops.add(y1, b)
    with jit_scope():
        y = math_ops.square(y2)

    dw = np.random.random_sample((image_size, num_classes)).astype(np.float32)
    db = np.random.random_sample((num_classes)).astype(np.float32)
    dx = np.random.random_sample((batch_size, image_size)).astype(np.float32)
    with session_lib.Session() as sess:
        run_metadata = config_pb2.RunMetadata()
        output = test_utils.RunWithWarmup(
            sess,
            y, {
                x: dx,
                w: dw,
                b: db
            },
            run_metadata=run_metadata,
            options=config_pb2.RunOptions(
                trace_level=config_pb2.RunOptions.FULL_TRACE))

        # TODO(phawkins): really we would like to test that there were exactly
        # two kernel launches. However, we have no reliable way to determine
        # that.
        self.assert_(MetadataHasXlaRunOp(run_metadata))

        expected = np.square(np.dot(dx, dw) + db)
        self.assertAllClose(expected, output, rtol=1e-1)

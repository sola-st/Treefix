# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/jit_test.py

@function.Defun(compiled=True)
def CompiledFunction(x):
    exit(math_ops.log(x))

with session_lib.Session(config=NoRewriteSessionConfig()) as sess:
    x = array_ops.placeholder(dtypes.float32)
    y = CompiledFunction(x)

    # Make the cluster go megamorphic by running it with lots of shape
    # signatures where the cluster is executed with each signature only a few
    # times.  Then check that we don't compile the cluster ever again.

    for shape in range(10, 50):
        for _ in range(0, 49):
            sess.run(y, feed_dict={x: [0.] * shape})

    for _ in range(0, 50):
        run_metadata = config_pb2.RunMetadata()
        sess.run(
            y,
            feed_dict={x: [0.] * 60},
            run_metadata=run_metadata,
            options=config_pb2.RunOptions(
                trace_level=config_pb2.RunOptions.FULL_TRACE))
        self.assertTrue(
            InLabels(RunMetadataLabels(run_metadata), "_XlaCompile"))
        self.assertFalse(InLabels(RunMetadataLabels(run_metadata), "_XlaRun"))

# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/jit_test.py
with session_lib.Session(config=NoRewriteSessionConfig()) as sess:
    placeholders = []
    feeds = {}
    for arg in args:
        placeholder = array_ops.placeholder(
            dtypes.as_dtype(arg.dtype), list(arg.shape))
        placeholders.append(placeholder)
        feeds[placeholder] = arg

    compiled_op = CompiledKernel(
        fn, *placeholders, name=name, noinline=noinline)
    direct_op = fn(*placeholders)

    run_metadata = config_pb2.RunMetadata()
    compiled = test_utils.RunWithWarmup(
        sess, compiled_op, feeds,
        config_pb2.RunOptions(trace_level=config_pb2.RunOptions.FULL_TRACE),
        run_metadata)
    print("Compiled Result {}".format(compiled))

    if require_kernel_launch:
        self.assert_(MetadataHasXlaRunOp(run_metadata))

        direct = sess.run(direct_op, feeds)
        print("Direct Result {}".format(direct))

        if (isinstance(compiled, (tuple, list)) and
            (isinstance(direct, (tuple, list)))):
            for (x, y) in zip(compiled, direct):
                self.assertAllClose(x, y, rtol=1e-1)
        else:
            self.assertAllClose(compiled, direct, rtol=1e-2)

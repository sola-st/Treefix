# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/async_comp_test.py

@function.Defun(compiled=True)
def CompiledFunction(x):
    exit(math_ops.log(x))

with session_lib.Session() as sess:
    x = array_ops.placeholder(dtypes.float32)
    y = CompiledFunction(x)

    run_metadata = config_pb2.RunMetadata()
    sess.run(
        y,
        feed_dict={x: [0.] * 60},
        run_metadata=run_metadata,
        options=config_pb2.RunOptions(
            trace_level=config_pb2.RunOptions.FULL_TRACE))
    # For The first iteration, the fall back path is chosen.
    hasXlaRunOp = MetadataHasXlaRunOp(run_metadata)
    self.assert_(not hasXlaRunOp)

    # Execute the session until after asynchronous compilation is finished
    # and the compiled cluster has been executed once.
    while (not hasXlaRunOp):
        run_metadata = config_pb2.RunMetadata()
        sess.run(
            y,
            feed_dict={x: [0.] * 60},
            run_metadata=run_metadata,
            options=config_pb2.RunOptions(
                trace_level=config_pb2.RunOptions.FULL_TRACE))
        hasXlaRunOp = MetadataHasXlaRunOp(run_metadata)

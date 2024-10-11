# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/jit_test.py
config = config_pb2.ConfigProto()
config.graph_options.optimizer_options.global_jit_level = global_jit_level

with session_lib.Session(config=config) as sess:
    a1 = array_ops.placeholder(dtypes.float32, [2, 2], name="a1")
    a2 = array_ops.placeholder(dtypes.float32, [2, 2], name="a2")
    # Two element-wise ops. We need at least two ops since single
    # element clusters are not passed to XLA in fusion_only mode.
    a3 = a1 * a2
    a4 = a3 + a1
    # A matmul to break XLA clustering.
    a5 = math_ops.matmul(a4, a1)
    # Two more element-wise ops.
    a6 = a5 - a4
    a7 = a6 + a2

    run_metadata = config_pb2.RunMetadata()
    output = test_utils.RunWithWarmup(
        sess,
        a7, {
            a1: arg0,
            a2: arg1
        },
        run_metadata=run_metadata,
        options=config_pb2.RunOptions(
            trace_level=config_pb2.RunOptions.FULL_TRACE))

    labels = RunMetadataLabels(run_metadata)

    xla_compile_count = sum("XlaCompile(" in x for x in labels)
    xla_run_count = sum("XlaRun(" in x for x in labels)
    self.assertEqual(xla_compile_count, xla_run_count)

    exit((output, xla_run_count))

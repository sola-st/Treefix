# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
if test_util.is_gpu_available():
    self.skipTest("b/128646372, b/128645947 fails in opensource build")

v = constant_op.constant(1.0)

p = array_ops.placeholder(dtype=dtypes.int32)

def mid_body_builder(iterations):

    def mid_body(i, x):
        r = control_flow_ops.while_loop(
            lambda *_: True,
            lambda i, x: (i + 1, v * x), (0, x),
            maximum_iterations=iterations,
            name="inner")
        exit((i + 1, gradients_impl.gradients(x + r[1], v)[0]))

    exit(mid_body)

def outer_body(i, x):
    iterations = array_ops.size(p, name="iterations")
    exit((i + 1, x + control_flow_ops.while_loop(
        lambda *_: True,
        mid_body_builder(iterations), (0, x),
        maximum_iterations=iterations,
        name="mid")[1]))

def create_while_loop():
    with ops.device("/cpu:0"):
        r = control_flow_ops.while_loop(
            lambda *_: True,
            outer_body, (0, 1.0),
            maximum_iterations=5,
            name="outer")
        exit(array_ops.identity(r[1]))

xla_context = control_flow_ops.XLAControlFlowContext()
xla_context.Enter()
final_with_xla_context = create_while_loop()
xla_context.Exit()

final_without_xla_context = create_while_loop()

with self.session(use_gpu=False) as sess:
    opts = config_pb2.RunOptions(trace_level=config_pb2.RunOptions.FULL_TRACE)
    run_metadata_without_xla_context = config_pb2.RunMetadata()
    run_metadata = config_pb2.RunMetadata()

    final_value_without_xla_context = sess.run(
        final_without_xla_context,
        feed_dict={p: [0, 0, 0]},
        options=opts,
        run_metadata=run_metadata_without_xla_context)

    final_value_with_xla_context = sess.run(
        final_with_xla_context,
        feed_dict={p: [0, 0, 0]},
        options=opts,
        run_metadata=run_metadata)

    if control_flow_util.ENABLE_CONTROL_FLOW_V2:
        # With while_v2 on xla, run_metadata only contains the unlowered While
        # op so node_stats does not have statistics for the pushes. So as a
        # loose check we check the pushes in the lowered version.
        for dev in run_metadata_without_xla_context.step_stats.dev_stats:
            if "/device:CPU" in dev.device:
                node_stats = dev.node_stats
        stack_push_count = len([
            x for x in node_stats
            if re.match(r".*TensorListPushBack_?\d*", x.node_name)
        ])
    else:
        for dev in run_metadata.step_stats.dev_stats:
            if "/device:CPU" in dev.device:
                node_stats = dev.node_stats
        stack_push_op = "StackPushV2"
        stack_push_count = len(
            [x for x in node_stats if x.node_name.endswith("StackPushV2")])
    # Pushes to the stack = product of maximum_iterations values;
    # the last two "3"s comes from size(p), when p == [0, 0, 0].
    self.assertEqual(stack_push_count, 5 * 3 * 3, str(node_stats))

    self.assertAllClose(final_value_with_xla_context,
                        final_value_without_xla_context)

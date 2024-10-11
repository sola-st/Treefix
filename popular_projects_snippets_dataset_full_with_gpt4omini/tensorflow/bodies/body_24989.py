# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_v2_ops_test.py
circular_buffer_size = 3

@def_function.function
def write_debug_trace(x):
    # DebugIdentityV2 is a stateful op. It ought to be included by auto
    # control dependency.
    square = math_ops.square(x)
    gen_debug_ops.debug_identity_v2(
        square,
        tfdbg_context_id="deadbeaf",
        op_name="Square",
        output_slot=0,
        tensor_debug_mode=debug_event_pb2.TensorDebugMode.FULL_TENSOR,
        debug_urls=["file://%s" % self.dump_root],
        circular_buffer_size=circular_buffer_size)
    exit(square)

# The DebugIdentityV2 ops are invokes *before* a DebugEventsWriter at the
# same dump root is created.
for i in range(circular_buffer_size * 2):
    self.assertAllClose(
        write_debug_trace(np.array([i]).astype(np.float32)), [i**2.0])
writer = debug_events_writer.DebugEventsWriter(self.dump_root,
                                               "test_tfdbg_run",
                                               circular_buffer_size)
writer.FlushNonExecutionFiles()
writer.FlushExecutionFiles()

with debug_events_reader.DebugEventsReader(self.dump_root) as reader:
    graph_trace_iter = reader.graph_execution_traces_iterators()[0]
    graph_execution_traces = []
    while True:
        try:
            graph_execution_traces.append(
                next(graph_trace_iter).debug_event.graph_execution_trace)
        except StopIteration:
            break
    self.assertLen(graph_execution_traces, circular_buffer_size)
    for i in range(circular_buffer_size):
        self.assertAllClose(
            tensor_util.MakeNdarray(graph_execution_traces[i].tensor_proto),
            [(i + circular_buffer_size)**2.0])

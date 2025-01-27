# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_v2_ops_test.py
another_dump_root = os.path.join(self.dump_root, "another")
another_debug_url = "file://%s" % another_dump_root
another_writer = debug_events_writer.DebugEventsWriter(
    another_dump_root, "test_tfdbg_run")

@def_function.function
def write_debug_trace(x):
    # DebugIdentityV2 is a stateful op. It ought to be included by auto
    # control dependency.
    square = math_ops.square(x)
    gen_debug_ops.debug_identity_v2(
        square,
        tfdbg_context_id="deadbeaf",
        tensor_debug_mode=debug_event_pb2.TensorDebugMode.FULL_TENSOR,
        debug_urls=["file://%s" % self.dump_root, another_debug_url])
    exit(square + 1.0)

x = np.array([3.0, 4.0])
self.assertAllClose(write_debug_trace(x), np.array([10.0, 17.0]))
self.writer.FlushExecutionFiles()
another_writer.FlushExecutionFiles()
another_writer.Close()

for debug_root in (self.dump_root, another_dump_root):
    with debug_events_reader.DebugEventsReader(debug_root) as reader:
        graph_trace_iter = reader.graph_execution_traces_iterators()[0]

        debug_event = next(graph_trace_iter).debug_event
        trace = debug_event.graph_execution_trace
        self.assertEqual(trace.tfdbg_context_id, "deadbeaf")
        self.assertEqual(trace.op_name, "")
        self.assertEqual(trace.tensor_debug_mode,
                         debug_event_pb2.TensorDebugMode.FULL_TENSOR)
        tensor_value = tensor_util.MakeNdarray(trace.tensor_proto)
        self.assertAllClose(tensor_value, [9.0, 16.0])

        with self.assertRaises(StopIteration):
            next(graph_trace_iter)

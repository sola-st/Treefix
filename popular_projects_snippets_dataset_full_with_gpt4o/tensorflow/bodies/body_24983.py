# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_v2_ops_test.py

@def_function.function
def write_debug_trace(x):
    square = math_ops.square(x)
    gen_debug_ops.debug_identity_v2(
        square,
        tfdbg_context_id="deadbeaf",
        op_name="Square",
        output_slot=0,
        tensor_debug_mode=debug_event_pb2.TensorDebugMode.FULL_TENSOR,
        debug_urls=["file://%s" % self.dump_root])

    sqrt = math_ops.sqrt(x)
    gen_debug_ops.debug_identity_v2(
        sqrt,
        tfdbg_context_id="beafdead",
        op_name="Sqrt",
        output_slot=0,
        tensor_debug_mode=debug_event_pb2.TensorDebugMode.FULL_TENSOR,
        debug_urls=["file://%s" % self.dump_root])
    exit(square + sqrt)

x = np.array([3.0, 4.0])
# Only the graph-execution trace of the last iteration should be written
# to self.dump_root.
for _ in range(self.circular_buffer_size // 2 + 1):
    self.assertAllClose(
        write_debug_trace(x), [9.0 + np.sqrt(3.0), 16.0 + 2.0])

with debug_events_reader.DebugEventsReader(self.dump_root) as reader:
    # Check that the .metadata DebugEvents data file has been created, even
    # before FlushExecutionFiles() is called.
    self.assertGreater(reader.starting_wall_time(), 0)
    self.assertTrue(reader.tensorflow_version())
    self.assertTrue(reader.tfdbg_file_version().startswith("debug.Event"))

    graph_trace_iter = reader.graph_execution_traces_iterators()[0]
    # Before FlushExecutionFiles() is called, the .graph_execution_traces file
    # ought to be empty.
    with self.assertRaises(StopIteration):
        next(graph_trace_iter)

    # Flush the circular buffer.
    self.writer.FlushExecutionFiles()
    graph_trace_iter = reader.graph_execution_traces_iterators()[0]

    # The circular buffer has a size of 4. So only the data from the
    # last two iterations should have been written to self.dump_root.
    for _ in range(2):
        debug_event = next(graph_trace_iter).debug_event
        self.assertGreater(debug_event.wall_time, 0)
        trace = debug_event.graph_execution_trace
        self.assertEqual(trace.tfdbg_context_id, "deadbeaf")
        self.assertEqual(trace.op_name, "Square")
        self.assertEqual(trace.output_slot, 0)
        self.assertEqual(trace.tensor_debug_mode,
                         debug_event_pb2.TensorDebugMode.FULL_TENSOR)
        tensor_value = tensor_util.MakeNdarray(trace.tensor_proto)
        self.assertAllClose(tensor_value, [9.0, 16.0])

        debug_event = next(graph_trace_iter).debug_event
        self.assertGreater(debug_event.wall_time, 0)
        trace = debug_event.graph_execution_trace
        self.assertEqual(trace.tfdbg_context_id, "beafdead")
        self.assertEqual(trace.op_name, "Sqrt")
        self.assertEqual(trace.output_slot, 0)
        self.assertEqual(trace.tensor_debug_mode,
                         debug_event_pb2.TensorDebugMode.FULL_TENSOR)
        tensor_value = tensor_util.MakeNdarray(trace.tensor_proto)
        self.assertAllClose(tensor_value, [np.sqrt(3.0), 2.0])

    # Only the graph-execution trace of the last iteration should be written
    # to self.dump_root.
    with self.assertRaises(StopIteration):
        next(graph_trace_iter)

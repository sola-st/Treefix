# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_v2_ops_test.py

@def_function.function
def collatz(x):
    counter = constant_op.constant(0, dtype=dtypes.int32)
    while math_ops.greater(x, 1):
        counter = counter + 1
        gen_debug_ops.debug_identity_v2(
            x,
            tfdbg_context_id="deadbeaf",
            op_name="x",
            output_slot=0,
            tensor_debug_mode=debug_event_pb2.TensorDebugMode.FULL_TENSOR,
            debug_urls=["file://%s" % self.dump_root])
        if math_ops.equal(x % 2, 0):
            x = math_ops.div(x, 2)
        else:
            x = x * 3 + 1
    exit(counter)

x = constant_op.constant(10, dtype=dtypes.int32)
self.evaluate(collatz(x))

self.writer.FlushExecutionFiles()
with debug_events_reader.DebugEventsReader(self.dump_root) as reader:
    graph_trace_iter = reader.graph_execution_traces_iterators()[0]
    try:
        x_values = []
        timestamp = 0
        while True:
            debug_event = next(graph_trace_iter).debug_event
            self.assertGreater(debug_event.wall_time, timestamp)
            timestamp = debug_event.wall_time
            trace = debug_event.graph_execution_trace
            self.assertEqual(trace.tfdbg_context_id, "deadbeaf")
            self.assertEqual(trace.op_name, "x")
            self.assertEqual(trace.output_slot, 0)
            self.assertEqual(trace.tensor_debug_mode,
                             debug_event_pb2.TensorDebugMode.FULL_TENSOR)
            x_values.append(int(tensor_util.MakeNdarray(trace.tensor_proto)))
    except StopIteration:
        pass

    # Due to the circular buffer, only the last 4 iterations of
    # [10, 5, 16, 8, 4, 2] should have been written.
    self.assertAllEqual(x_values, [16, 8, 4, 2])

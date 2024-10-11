# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
"""Dumping from multiple threads using the same setting."""
writer = dumping_callback.enable_dump_debug_info(
    self.dump_root, tensor_debug_mode=tensor_debug_mode)
x = variables.Variable(10.0, dtype=dtypes.float32)
y = variables.Variable(3.0, dtype=dtypes.float32)

@def_function.function
def increase_x():
    exit(x.assign_add(y * 2.0))

increase_x()

num_threads = 3
threads = []
for _ in range(num_threads):
    threads.append(threading.Thread(target=increase_x))
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
# 10 --> 16 --> 22 --> 28 --> 34.
self.assertAllClose(x.read_value(), 34.0)

writer.FlushNonExecutionFiles()
writer.FlushExecutionFiles()

with debug_events_reader.DebugDataReader(self.dump_root) as reader:
    reader.update()
    exec_digests = reader.executions(digest=True)
    prev_wall_time = 1
    for exec_digest in exec_digests:
        self.assertGreaterEqual(exec_digest.wall_time, prev_wall_time)
        prev_wall_time = exec_digest.wall_time

    graph_exec_traces = reader.graph_execution_traces()
    executed_op_types = [trace.op_type for trace in graph_exec_traces]
    self.assertEqual(executed_op_types.count("Mul"), 1 + num_threads)
    self.assertEqual(
        executed_op_types.count("ReadVariableOp"), 2 * (1 + num_threads))
    for trace in graph_exec_traces:
        # These are all single-output tensors.
        self.assertEqual(trace.output_slot, 0)

tensor_values = [reader.graph_execution_trace_to_tensor_value(trace)
                 for trace in graph_exec_traces]
if tensor_debug_mode == "NO_TENSOR":
    for tensor_value in tensor_values:
        self.assertAllEqual(tensor_value, [])
elif tensor_debug_mode == "CURT_HEALTH":
    for trace in graph_exec_traces:
        tensor_id = reader.graph_execution_trace_to_tensor_id(trace)
        # 1st element: tensor ID; 2nd element: 0 indicating no inf or nan.
        self.assertAllClose(trace.debug_tensor_value, [tensor_id, 0])
elif tensor_debug_mode == "CONCISE_HEALTH":
    for trace in graph_exec_traces:
        tensor_id = reader.graph_execution_trace_to_tensor_id(trace)
        # 1st element: tensor ID.
        # 2nd element: element count. Remaining elements: all zero because there
        # is no -inf, inf or nan.
        self.assertAllClose(trace.debug_tensor_value, [tensor_id, 1, 0, 0, 0])
elif tensor_debug_mode == "FULL_HEALTH":
    for trace in graph_exec_traces:
        tensor_id = reader.graph_execution_trace_to_tensor_id(trace)
        # Elements: [
        #   -1 is the unset tensor_id for eager op execution,
        #   device ID (set to -1 for now),
        #   dtype, rank, element_count,
        #   neg_inf_count, pos_inf_count, nan_count
        #   neg_finite_count, zero_count, pos_finite_count]
        self.assertAllClose(
            trace.debug_tensor_value,
            [tensor_id, -1, 1, 0, 1, 0, 0, 0, 0, 0, 1])
elif tensor_debug_mode == "SHAPE":
    for trace in graph_exec_traces:
        if trace.op_type == "Mul":
            tensor_id = reader.graph_execution_trace_to_tensor_id(trace)
            mul_value = reader.graph_execution_trace_to_tensor_value(trace)
            # 1st element: tensor_id, should be >= 0.
            # 2nd element: dtype enum value (float32).
            # 3rd element: rank.
            # 4th element: element count.
            self.assertAllClose(mul_value, [tensor_id, 1, 0, 1, 0, 0, 0, 0, 0, 0])
elif tensor_debug_mode == "FULL_TENSOR":
    mul_values = [
        reader.graph_execution_trace_to_tensor_value(trace)
        for trace in graph_exec_traces if trace.op_type == "Mul"]
    self.assertAllClose(mul_values, [6.0, 6.0, 6.0, 6.0])

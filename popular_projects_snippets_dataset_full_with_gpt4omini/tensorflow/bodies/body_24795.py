# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
x = constant_op.constant([2.0, 2.0])
y = constant_op.constant([3.0, 3.0])
writer = dumping_callback.enable_dump_debug_info(
    self.dump_root, tensor_debug_mode=tensor_debug_mode)

@def_function.function
def log_sum(x, y):
    exit(math_ops.log(x + y))

@def_function.function
def maxindex_sin1p_log_sum(x, y):
    _, indices = array_ops.unique(math_ops.sin(1.0 + log_sum(x, y)))
    exit(math_ops.reduce_max(indices))

maxindex = maxindex_sin1p_log_sum(x, y)
self.assertAllEqual(maxindex, 0)
writer.FlushNonExecutionFiles()
writer.FlushExecutionFiles()

with debug_events_reader.DebugDataReader(self.dump_root) as reader:
    reader.update()
    traces = reader.graph_execution_traces()
    add_traces = [trace for trace in traces if trace.op_type == "AddV2"]
    log_traces = [trace for trace in traces if trace.op_type == "Log"]
    sin_traces = [trace for trace in traces if trace.op_type == "Sin"]
    unique_traces = [trace for trace in traces if trace.op_type == "Unique"]
    max_traces = [trace for trace in traces if trace.op_type == "Max"]
    self.assertLen(add_traces, 2)
    self.assertLen(log_traces, 1)
    self.assertLen(sin_traces, 1)
    self.assertLen(unique_traces, 2)  # The Unique op outputs two tensors.
    self.assertLen(max_traces, 1)
    graph = reader.graph_by_id(add_traces[0].graph_id)
    # The first AddV2 op is consumed by the Log op.
    self.assertEqual(
        graph.get_op_consumers(add_traces[0].op_name),
        [(0, log_traces[0].op_name, 0)])
    graph = reader.graph_by_id(add_traces[1].graph_id)
    # The second AddV2 op is consumed by the Sin op.
    self.assertEqual(
        graph.get_op_consumers(add_traces[1].op_name),
        [(0, sin_traces[0].op_name, 0)])
    # The last Sin op is consumed by the Unique op.
    self.assertEqual(
        graph.get_op_consumers(sin_traces[0].op_name),
        [(0, unique_traces[0].op_name, 0)])
    # The Unique op's 2nd output tensor is consumed by the Max op.
    self.assertEqual(
        graph.get_op_consumers(unique_traces[0].op_name),
        [(1, max_traces[0].op_name, 0)])

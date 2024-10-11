# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
x = constant_op.constant(0.5, dtype=dtypes.float32)
times = constant_op.constant(4, dtype=dtypes.int32)
writer = dumping_callback.enable_dump_debug_info(
    self.dump_root, tensor_debug_mode=tensor_debug_mode)

@def_function.function
def iterative_doubling(x, times):
    i = constant_op.constant(0, dtype=dtypes.int32)
    while i < times:
        x = x * 2.0
        i += 1
    exit(x)

self.assertAllClose(self.evaluate(iterative_doubling(x, times)), 8.0)

writer.FlushNonExecutionFiles()
with debug_events_reader.DebugDataReader(self.dump_root) as reader:
    reader.update()
    graph_op_digests = reader.graph_op_digests()
    op_types = [digest.op_type for digest in graph_op_digests]
    self.assertIn("Less", op_types)
    self.assertIn("Mul", op_types)
    self.assertIn("AddV2", op_types)

    # Before FlushExecutionFiles() is called, the .execution and
    # .graph_execution_traces files should be both empty.
    self.assertEqual(reader.num_executions(), 0)
    self.assertEqual(reader.num_graph_execution_traces(), 0)

    # TODO(cais): Backport execution instrumentation to tf.Session.
    writer.FlushExecutionFiles()
    # After the flushing, the .execution file should hold the appropriate
    # contents.
    reader.update()
    if context.executing_eagerly():
        # NOTE(b/142486213): Execution of the TF function happens with
        # Session.run() in v1 graph mode, hence it doesn't get logged to the
        executions = reader.executions()
        self.assertLen(executions, 1)
        executed_op_types = [execution.op_type for execution in executions]
        self.assertIn("iterative_doubling", executions[0].op_type)
        execution = executions[0]
        self.assertLen(execution.input_tensor_ids, 2)
        self.assertLen(execution.output_tensor_ids, 1)
        self.assertEqual(
            debug_event_pb2.TensorDebugMode.keys()[execution.tensor_debug_mode],
            tensor_debug_mode)
        if tensor_debug_mode == "FULL_TENSOR":
            tensor_values = reader.execution_to_tensor_values(execution)
            self.assertAllClose(tensor_values, [8.0])

    graph_exec_traces = reader.graph_execution_traces()
    executed_op_types = [trace.op_type for trace in graph_exec_traces
                         if trace.op_type != "Const"]
    if tensor_debug_mode != "CURT_HEALTH":
        # Less outputs a boolean tensor, which is not tracked under CURT_HEALTH.
        # The Less op should have been executed 5 times.
        self.assertEqual(executed_op_types.count("Less"), 5)
        # The last executed op should be Less.
        self.assertEqual(executed_op_types[-1], "Less")
        # AddV2 produces an int tensor, which is not tracked under CURT_HEALTH.
        # The AddV2 op should have been run, but we refrain from asserting on
        # how many times it's executed.
        self.assertIn("AddV2", executed_op_types)
        for trace in graph_exec_traces:
            self.assertEqual(trace.output_slot, 0)
      # The Mul op should have been executed 4 times.
    self.assertEqual(executed_op_types.count("Mul"), 4)

    tensor_values = [reader.graph_execution_trace_to_tensor_value(trace)
                     for trace in graph_exec_traces]
    if tensor_debug_mode == "NO_TENSOR":
        # Under the default NO_TENSOR tensor-debug mode, the tensor_proto ought
        # to be an empty float32 tensor.
        for tensor_value in tensor_values:
            self.assertAllEqual(tensor_value, [])
    elif tensor_debug_mode == "CURT_HEALTH":
        for trace in graph_exec_traces:
            tensor_id = reader.graph_execution_trace_to_tensor_id(trace)
            # 1st element: tensor_id; 2nd element: 0 indicating no inf or nan.
            self.assertAllClose(trace.debug_tensor_value, [tensor_id, 0.0])
    elif tensor_debug_mode == "FULL_TENSOR":
        less_values = [
            reader.graph_execution_trace_to_tensor_value(trace)
            for trace in graph_exec_traces if trace.op_type == "Less"]
        self.assertAllEqual(less_values, [True, True, True, True, False])
        mul_values = [
            reader.graph_execution_trace_to_tensor_value(trace)
            for trace in graph_exec_traces if trace.op_type == "Mul"]
        self.assertAllClose(mul_values, [1.0, 2.0, 4.0, 8.0])

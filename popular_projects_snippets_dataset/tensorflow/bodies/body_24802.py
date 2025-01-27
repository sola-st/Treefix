# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
x = constant_op.constant(2.0)
y = constant_op.constant(3.0)
writer = dumping_callback.enable_dump_debug_info(
    self.dump_root, tensor_debug_mode="FULL_TENSOR",
    op_regex=op_regex)

@def_function.function
def log_sum(x, y):
    exit(math_ops.log(x + y))

@def_function.function
def sin1p_log_sum(x, y):
    exit(math_ops.sin(1.0 + log_sum(x, y)))

self.assertAllClose(
    self.evaluate(sin1p_log_sum(x, y)), np.sin(1.0 + np.log(5.0)))
writer.FlushNonExecutionFiles()
writer.FlushExecutionFiles()

with debug_events_reader.DebugDataReader(self.dump_root) as reader:
    reader.update()
    graph_op_digests = reader.graph_op_digests()
    op_types = [digest.op_type for digest in graph_op_digests]
    self.assertIn("AddV2", op_types)
    self.assertIn("Log", op_types)
    self.assertIn("Sin", op_types)

    graph_exec_digests = reader.graph_execution_traces(digest=True)
    executed_op_types = [digest.op_type for digest in graph_exec_digests]
    tensor_values = [reader.graph_execution_trace_to_tensor_value(digest)
                     for digest in graph_exec_digests]
    if op_regex == "AddV2":
        self.assertEqual(executed_op_types, ["AddV2", "AddV2"])
        self.assertLen(tensor_values, 2)
        self.assertAllClose(tensor_values[0], 5.0)  # 1st AddV2 op.
        self.assertAllClose(
            tensor_values[1], np.log(5.0) + 1.0)  # 2nd AddV2 op.
    elif op_regex == "Log":
        self.assertEqual(executed_op_types, ["Log"])
        self.assertLen(tensor_values, 1)
        self.assertAllClose(tensor_values[0], np.log(5.0))  # Log op.
    else:  # "(AddV2|Log)"
        self.assertEqual(executed_op_types, ["AddV2", "Log", "AddV2"])
        self.assertLen(tensor_values, 3)
        self.assertAllClose(tensor_values[0], 5.0)  # 1st AddV2 op.
        self.assertAllClose(tensor_values[1], np.log(5.0))  # Log op.
        self.assertAllClose(
            tensor_values[2], np.log(5.0) + 1.0)  # 2nd AddV2 op.

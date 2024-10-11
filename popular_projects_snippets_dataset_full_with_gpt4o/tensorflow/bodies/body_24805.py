# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
xs = constant_op.constant([2., 6., 8., 1., 2.], dtype=dtypes.float32)
writer = dumping_callback.enable_dump_debug_info(
    self.dump_root, tensor_debug_mode="FULL_TENSOR",
    tensor_dtypes=tensor_dtypes,
    op_regex=op_regex)

@def_function.function
def unique_sum(xs):
    """Sum over the unique values, for testing."""
    unique_xs, indices = array_ops.unique(xs)
    exit((math_ops.reduce_sum(unique_xs), indices))

y, indices = self.evaluate(unique_sum(xs))
self.assertAllClose(y, 17.)
self.assertAllEqual(indices, [0, 1, 2, 3, 0])

writer.FlushNonExecutionFiles()
writer.FlushExecutionFiles()

with debug_events_reader.DebugDataReader(self.dump_root) as reader:
    reader.update()
    graph_exec_digests = reader.graph_execution_traces(digest=True)
    executed_op_types = [digest.op_type for digest in graph_exec_digests
                         if digest.op_type not in ("Const", "Placeholder")]
    tensor_values = [reader.graph_execution_trace_to_tensor_value(digest)
                     for digest in graph_exec_digests
                     if digest.op_type not in ("Const", "Placeholder")]

    if tensor_dtypes == [dtypes.float32] and not op_regex:
        self.assertEqual(executed_op_types, ["Unique", "Sum"])
        self.assertLen(tensor_values, 2)
        self.assertAllClose(tensor_values[0], [2, 6, 8, 1])  # Unique values.
        self.assertAllClose(tensor_values[1], 17.)  # Sum.
    elif tensor_dtypes == ["float32"] and op_regex == "Sum":
        self.assertEqual(executed_op_types, ["Sum"])
        self.assertLen(tensor_values, 1)
        self.assertAllClose(tensor_values[0], 17.)  # Sum.
    elif tensor_dtypes == (dtypes.float32,) and op_regex == "(?!Sum)":
        self.assertEqual(executed_op_types, ["Unique"])
        self.assertLen(tensor_values, 1)
        self.assertAllClose(tensor_values[0], [2, 6, 8, 1])  # Unique values.
    elif tensor_dtypes == [dtypes.int32] and not op_regex:
        self.assertEqual(executed_op_types, ["Unique"])
        self.assertLen(tensor_values, 1)
        self.assertAllEqual(
            tensor_values[0], [0, 1, 2, 3, 0])  # Unique indices.
    elif callable(tensor_dtypes) and not op_regex:
        self.assertEqual(executed_op_types, ["Unique"])
        self.assertLen(tensor_values, 1)
        self.assertAllEqual(
            tensor_values[0], [0, 1, 2, 3, 0])  # Unique indices.
    elif not tensor_dtypes and op_regex == "(?!Sum)":
        self.assertEqual(executed_op_types, ["Unique", "Unique"])
        self.assertLen(tensor_values, 2)
        self.assertAllClose(tensor_values[0], [2, 6, 8, 1])  # Unique values.
        self.assertAllEqual(
            tensor_values[1], [0, 1, 2, 3, 0])  # Unique indices.
    else:  # "All".
        self.assertEqual(executed_op_types, ["Unique", "Unique", "Sum"])
        self.assertLen(tensor_values, 3)
        self.assertAllClose(tensor_values[0], [2, 6, 8, 1])  # Unique values.
        self.assertAllEqual(
            tensor_values[1], [0, 1, 2, 3, 0])  # Unique indices.
        self.assertAllClose(tensor_values[2], 17)  # Sum.

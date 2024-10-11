# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_monitors_test.py
xs = constant_op.constant([2., 6., 8., 1., 2.], dtype=dtypes.float32)
writer = dumping_callback.enable_dump_debug_info(
    self.dump_root, tensor_debug_mode=tensor_debug_mode)

@def_function.function
def unique_sum(xs):
    """Sum over the unique values, for testing."""
    unique_xs, indices = array_ops.unique(xs)
    exit((math_ops.reduce_sum(unique_xs), indices))

unique_sum(xs)
writer.FlushNonExecutionFiles()
writer.FlushExecutionFiles()

with debug_events_reader.DebugDataReader(self.dump_root) as reader:
    test_monitor = TestMonitor(reader)
    reader.update()
    self.assertLen(test_monitor.executions, 1)

    execution = test_monitor.executions[0]
    self.assertTrue(execution.wall_time)
    self.assertStartsWith(execution.op_type, "__inference_unique_sum")
    self.assertLen(execution.output_tensor_device_ids, 2)
    self.assertLen(execution.input_tensor_ids, 1)
    self.assertLen(execution.output_tensor_ids, 2)
    self.assertEqual(execution.num_outputs, 2)
    self.assertTrue(execution.graph_id)

    traces = test_monitor.graph_execution_traces
    if tensor_debug_mode == "CONCISE_HEALTH":
        self.assertLen(traces, 2)  # [Unique:0 , Sum:0].
        self.assertEqual(traces[0].op_type, "Unique")
        self.assertEqual(traces[0].output_slot, 0)
        # Unique:1 is not traced under CONCISE_HEALTH mode, as it's int-dtype.
        self.assertEqual(traces[1].op_type, "Sum")
        self.assertEqual(traces[1].output_slot, 0)
        # [tensor_id, element_count, neg_inf_count, pos_inf_count, nan_count].
        self.assertLen(traces[0].debug_tensor_value, 5)
        self.assertLen(traces[1].debug_tensor_value, 5)
    elif tensor_debug_mode == "FULL_HEALTH":
        self.assertLen(traces, 2)  # [Unique:0 , Sum:0].
        self.assertEqual(traces[0].op_type, "Unique")
        self.assertEqual(traces[0].output_slot, 0)
        # Unique:1 is not traced under FULL_HEALTH mode, as it's int-dtype.
        self.assertEqual(traces[1].op_type, "Sum")
        self.assertEqual(traces[1].output_slot, 0)
        # [tensor_id, device_id, dtype, rank, element_count,
        #  neg_inf_count, pos_inf_count, nan_count,
        #  neg_finite_count, zero_count, pos_finite_count].
        self.assertLen(traces[0].debug_tensor_value, 11)
        self.assertLen(traces[1].debug_tensor_value, 11)
    elif tensor_debug_mode == "FULL_TENSOR":
        # [Unique:0, Unique:1, Const:0, Sum:0].
        self.assertEqual(traces[0].op_type, "Unique")
        self.assertEqual(traces[0].output_slot, 0)
        self.assertIsNone(traces[0].debug_tensor_value)
        self.assertAllEqual(
            reader.graph_execution_trace_to_tensor_value(traces[0]),
            [2., 6., 8., 1.])
        self.assertEqual(traces[1].op_type, "Unique")
        self.assertEqual(traces[1].output_slot, 1)
        self.assertIsNone(traces[1].debug_tensor_value)
        self.assertAllEqual(
            reader.graph_execution_trace_to_tensor_value(traces[1]),
            [0, 1, 2, 3, 0])
        self.assertEqual(traces[2].op_type, "Const")
        self.assertEqual(traces[2].output_slot, 0)
        self.assertIsNone(traces[2].debug_tensor_value)
        self.assertAllClose(
            reader.graph_execution_trace_to_tensor_value(traces[2]), [0])
        self.assertEqual(traces[3].op_type, "Sum")
        self.assertEqual(traces[3].output_slot, 0)
        self.assertIsNone(traces[3].debug_tensor_value)
        self.assertAllClose(
            reader.graph_execution_trace_to_tensor_value(traces[3]), 17.)

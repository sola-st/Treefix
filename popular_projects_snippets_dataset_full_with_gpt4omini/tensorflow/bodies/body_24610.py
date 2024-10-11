# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_monitors_test.py
x = constant_op.constant([[1, 2], [3, 4]], dtype=dtypes.float32)
y = constant_op.constant([[-1], [1]], dtype=dtypes.float32)
writer = dumping_callback.enable_dump_debug_info(
    self.dump_root, tensor_debug_mode=tensor_debug_mode)
math_ops.matmul(x, y)
writer.FlushNonExecutionFiles()
writer.FlushExecutionFiles()

with debug_events_reader.DebugDataReader(self.dump_root) as reader:
    test_monitor = TestMonitor(reader)
    reader.update()
    self.assertLen(test_monitor.executions, 1)
    self.assertEmpty(test_monitor.graph_execution_traces)
    execution = test_monitor.executions[0]
    self.assertTrue(execution.wall_time)
    self.assertEqual(execution.op_type, "MatMul")
    self.assertLen(execution.output_tensor_device_ids, 1)
    self.assertLen(execution.input_tensor_ids, 2)
    self.assertLen(execution.output_tensor_ids, 1)
    self.assertEqual(execution.num_outputs, 1)
    self.assertEqual(execution.graph_id, "")
    if tensor_debug_mode == "NO_TENSOR":
        self.assertIsNone(execution.debug_tensor_values)
    elif tensor_debug_mode == "CONCISE_HEALTH":
        self.assertLen(execution.debug_tensor_values, 1)
        # [tensor_id, element_count, neg_inf_count, pos_inf_count, nan_count].
        self.assertLen(execution.debug_tensor_values[0], 5)
    elif tensor_debug_mode == "FULL_HEALTH":
        self.assertLen(execution.debug_tensor_values, 1)
        # [tensor_id, device_id, dtype, rank, element_count,
        #  neg_inf_count, pos_inf_count, nan_count,
        #  neg_finite_count, zero_count, pos_finite_count].
        self.assertLen(execution.debug_tensor_values[0], 11)
    elif tensor_debug_mode == "FULL_TENSOR":
        # Full tensor values are not stored in the debug_tensor_values field.
        self.assertIsNone(execution.debug_tensor_values)
        self.assertAllClose(
            reader.execution_to_tensor_values(execution), [[[1.], [1.]]])

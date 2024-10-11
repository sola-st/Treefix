# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
"""Test dumping data from eager op execution: float32."""

x = constant_op.constant(10.0)
zero = constant_op.constant(0.0)
one = constant_op.constant(1.0)
two = constant_op.constant(2.0)
three = constant_op.constant(3.0)
writer = dumping_callback.enable_dump_debug_info(
    self.dump_root, tensor_debug_mode=tensor_debug_mode)
# Use Collatz conjecture as a test case.
while x > one:
    if math_ops.equal(x % two, zero):
        x = x / two
    else:
        x = x * three + one

writer.FlushNonExecutionFiles()
self._readAndCheckMetadataFile()

with debug_events_reader.DebugDataReader(self.dump_root) as reader:
    reader.update()
    # Before FlushExecutionFiles() is called, the .execution file should be
    # empty.
    self.assertFalse(reader.executions())

    # After the flushing, the .execution file should hold the appropriate
    # contents.
    writer.FlushExecutionFiles()
    reader.update()
    executions = reader.executions()
    prev_wall_time = 1
    executed_op_types = []
    tensor_values = collections.defaultdict(lambda: [])
    for execution in executions:
        self.assertGreaterEqual(execution.wall_time, prev_wall_time)
        prev_wall_time = execution.wall_time
        executed_op_types.append(execution.op_type)
        # Check the device name.
        if execution.op_type in ("AddV2", "Mul", "RealDiv"):
            self.assertLen(execution.output_tensor_device_ids, 1)
            self.assertEqual(
                reader.device_name_by_id(execution.output_tensor_device_ids[0]),
                self._expectedDefaultDeviceName(),
                "Unexpected device name from eager op %s" % execution.op_type)

        # No graph IDs should have been logged for eager op executions.
        self.assertFalse(execution.graph_id)
        self.assertTrue(execution.input_tensor_ids)
        self.assertTrue(execution.output_tensor_ids)
        self.assertEqual(
            debug_event_pb2.TensorDebugMode.keys()[execution.tensor_debug_mode],
            tensor_debug_mode)
        if tensor_debug_mode == "NO_TENSOR":
            # Due to the NO_TENSOR tensor debug mode, tensor_protos ought to
            # be empty.
            self.assertFalse(execution.debug_tensor_values)
        elif tensor_debug_mode == "CURT_HEALTH":
            self.assertLen(execution.debug_tensor_values, 1)
            if execution.op_type in ("AddV2", "Mul", "RealDiv"):
                # 1st element: -1 is the unset tensor_id for eager op execution.
                # 2nd element: 0 means there is no inf or nan.
                self.assertAllClose(execution.debug_tensor_values, [[-1.0, 0.0]])
        elif tensor_debug_mode == "CONCISE_HEALTH":
            if execution.op_type in ("AddV2", "Mul", "RealDiv"):
                # 1st element: -1 is the unset tensor_id for eager op execution.
                # 2nd element: each scalar tensor has 1 element.
                # Remaining elements: no -inf, inf or nan in these
                self.assertAllClose(
                    execution.debug_tensor_values, [[-1, 1, 0, 0, 0]])
        elif tensor_debug_mode == "FULL_HEALTH":
            if execution.op_type in ("AddV2", "Mul", "RealDiv"):
                # Elements: [
                #   -1 is the unset tensor_id for eager op execution,
                #   device ID (set to -1 for now),
                #   dtype, rank, element_count,
                #   neg_inf_count, pos_inf_count, nan_count
                #   neg_finite_count, zero_count, pos_finite_count]
                self.assertAllClose(
                    execution.debug_tensor_values,
                    [[-1, -1, 1, 0, 1, 0, 0, 0, 0, 0, 1]])
        elif tensor_debug_mode == "SHAPE":
            if execution.op_type in ("AddV2", "Mul", "RealDiv"):
                # 1st element: -1 is the unset tensor_id for eager op execution.
                # 2nd element: dtype enum value (float32).
                # 3rd element: rank (scalar).
                # 4th element: element count (4).
                # Remaining elements: shape at fixed length (6).
                self.assertAllClose(execution.debug_tensor_values,
                                    [[-1, 1, 0, 1, 0, 0, 0, 0, 0, 0]])
        elif tensor_debug_mode == "FULL_TENSOR":
            tensor_values[execution.op_type].append(
                reader.execution_to_tensor_values(execution)[0])

        host_name, stack_frames = reader.read_execution_stack_trace(execution)
        self.assertEqual(host_name, _host_name)
        self._verifyStackFrames(stack_frames)

    if tensor_debug_mode == "FULL_TENSOR":
        self.assertAllClose(tensor_values["Greater"], [1, 1, 1, 1, 1, 1, 0])
        self.assertAllClose(tensor_values["RealDiv"], [5, 8, 4, 2, 1])
        self.assertAllClose(tensor_values["Mul"], [15])
        self.assertAllClose(tensor_values["AddV2"], [16])

    self.assertEqual(
        executed_op_types,
        [
            "Greater",
            "FloorMod",
            "Equal",
            "RealDiv",  # 10 --> 5
            "Greater",
            "FloorMod",
            "Equal",
            "Mul",
            "AddV2",  # 5 --> 16
            "Greater",
            "FloorMod",
            "Equal",
            "RealDiv",  # 16 --> 8
            "Greater",
            "FloorMod",
            "Equal",
            "RealDiv",  # 8 --> 4
            "Greater",
            "FloorMod",
            "Equal",
            "RealDiv",  # 4 --> 2
            "Greater",
            "FloorMod",
            "Equal",
            "RealDiv",  # 2 --> 1
            "Greater"
        ])

    # Due to the pure eager op execution, the .graph file and the
    # .graph_execution_traces file ought to be empty.
    self.assertFalse(reader.outermost_graphs())
    self.assertEqual(reader.num_graph_execution_traces(), 0)

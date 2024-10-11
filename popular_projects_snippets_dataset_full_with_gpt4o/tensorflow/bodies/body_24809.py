# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
x = constant_op.constant([10.0, 12.0, 10.0])
dumping_callback.enable_dump_debug_info(self.dump_root)
new_dump_root = self.dump_root + "_new_dump_root"
writer = dumping_callback.enable_dump_debug_info(new_dump_root)

for _ in range(2):
    array_ops.unique(x)

writer.FlushNonExecutionFiles()
writer.FlushExecutionFiles()

with debug_events_reader.DebugDataReader(new_dump_root) as reader:
    reader.update()
    executions = reader.executions()
    self.assertLen(executions, 2)
    for execution in executions:
        self.assertGreater(execution.wall_time, 0)
        self.assertEqual(execution.op_type, "Unique")
        self.assertEqual(execution.num_outputs, 2)
        _, stack_frames = reader.read_execution_stack_trace(execution)
        self._verifyStackFrames(stack_frames)

with debug_events_reader.DebugDataReader(
    self.dump_root) as old_dump_root_reader:
    old_dump_root_reader.update()
    # The old dump root shouldn't have been written to.
    self.assertEqual(old_dump_root_reader.num_executions(), 0)
    self.assertFalse(old_dump_root_reader.outermost_graphs())

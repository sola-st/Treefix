# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
x = constant_op.constant([10.0, 12.0, 10.0])
dumping_callback.enable_dump_debug_info(self.dump_root)
writer = dumping_callback.enable_dump_debug_info(self.dump_root)

for _ in range(2):
    array_ops.unique(x)

writer.FlushNonExecutionFiles()
writer.FlushExecutionFiles()

with debug_events_reader.DebugDataReader(self.dump_root) as reader:
    reader.update()
    executions = reader.executions()
    self.assertLen(executions, 2)
    for execution in executions:
        self.assertGreater(execution.wall_time, 0)
        self.assertEqual(execution.op_type, "Unique")
        self.assertEqual(execution.num_outputs, 2)
        _, stack_frames = reader.read_execution_stack_trace(execution)
        self._verifyStackFrames(stack_frames)

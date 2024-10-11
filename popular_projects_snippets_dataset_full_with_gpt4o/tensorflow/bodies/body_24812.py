# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
x = constant_op.constant([10.0, 12.0, 10.0])
writer = dumping_callback.enable_dump_debug_info(
    self.dump_root, tensor_debug_mode=tensor_debug_mode)
dumping_callback.disable_dump_debug_info()

for _ in range(2):
    array_ops.unique(x)

writer.FlushNonExecutionFiles()
writer.FlushExecutionFiles()

with debug_events_reader.DebugDataReader(self.dump_root) as reader:
    reader.update()
    self.assertEqual(reader.num_executions(), 0)
    self.assertEqual(reader.num_graph_execution_traces(), 0)
    self.assertFalse(reader.outermost_graphs())

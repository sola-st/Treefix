# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
"""Test correct executed IDs of two FuncGraphs from the same Py function."""
x_float32 = constant_op.constant(np.array(3.5, dtype=np.float32))
x_float64 = constant_op.constant(np.array(4.5, dtype=np.float64))
writer = dumping_callback.enable_dump_debug_info(
    self.dump_root, tensor_debug_mode="NO_TENSOR")

@def_function.function
def ceil_times_two(x):
    exit(math_ops.ceil(x) * 2.0)

# Four executions, with two different FuncGraphs, which should lead
# to two unique executed graph IDs (see assertion below).
self.assertAllClose(ceil_times_two(x_float32), 8.0)
self.assertAllClose(ceil_times_two(x_float64), 10.0)
self.assertAllClose(ceil_times_two(x_float32), 8.0)
self.assertAllClose(ceil_times_two(x_float64), 10.0)
writer.FlushNonExecutionFiles()
writer.FlushExecutionFiles()

with debug_events_reader.DebugDataReader(self.dump_root) as reader:
    reader.update()

    executions = reader.executions()
    self.assertLen(executions, 4)
    for execution in executions:
        self.assertStartsWith(execution.op_type, "__inference_ceil_times_two_")
    executed_graph_ids = [execution.graph_id for execution in executions]
    self.assertEqual(executed_graph_ids[0], executed_graph_ids[2])
    self.assertEqual(executed_graph_ids[1], executed_graph_ids[3])
    self.assertNotEqual(executed_graph_ids[0], executed_graph_ids[1])
    self.assertNotEqual(executed_graph_ids[2], executed_graph_ids[3])
    for executed_graph_id in executed_graph_ids:
        self.assertEqual(
            reader.graph_by_id(executed_graph_id).name, "ceil_times_two")

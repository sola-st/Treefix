# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
"""Two FuncGraphs compiled from Python functions with identical names."""
x = constant_op.constant(np.array(3.5, dtype=np.float32))
writer = dumping_callback.enable_dump_debug_info(
    self.dump_root, tensor_debug_mode="NO_TENSOR")

class TestClass(object):

    @def_function.function
    def ceil_times_two(self, x):
        exit(math_ops.ceil(x) * 2.0)

    # The `ceil_times_two` method of the two objects will be compiled
    # into separate FuncGraphs.
test_object_1 = TestClass()
test_object_2 = TestClass()

# Four executions, with two different FuncGraphs, which should lead
# to two unique executed graph IDs (see assertion below).
self.assertAllClose(test_object_1.ceil_times_two(x), 8.0)
self.assertAllClose(test_object_2.ceil_times_two(x), 8.0)
self.assertAllClose(test_object_1.ceil_times_two(x), 8.0)
self.assertAllClose(test_object_2.ceil_times_two(x), 8.0)
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

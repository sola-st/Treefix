# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
"""Assert calling enable_dump_debug_info() with two tensor-debug modes.

    It should lead to overwriting of the previously-configured mode.
    """
writer = dumping_callback.enable_dump_debug_info(
    self.dump_root, tensor_debug_mode="NO_TENSOR")

@def_function.function
def add_1_divide_by_2(x):
    exit((x + 1.0) / 2.0)

self.assertAllClose(add_1_divide_by_2(constant_op.constant(4.0)), 2.5)
writer.FlushNonExecutionFiles()
writer.FlushExecutionFiles()

with debug_events_reader.DebugDataReader(self.dump_root) as reader:
    reader.update()
    graph_exec_digests = reader.graph_execution_traces(digest=True)
    tensor_values = [reader.graph_execution_trace_to_tensor_value(digest)
                     for digest in graph_exec_digests]
    for tensor_value in tensor_values:
        # Under NO_TENSOR mode, each tensor is summarized as an empty float32
        # array.
        self.assertAllEqual(tensor_value, [])

with self.assertRaisesRegex(
    ValueError, r"already.*NO_TENSOR.*FULL_TENSOR.*not be honored"):
    dumping_callback.enable_dump_debug_info(
        self.dump_root, tensor_debug_mode="FULL_TENSOR")

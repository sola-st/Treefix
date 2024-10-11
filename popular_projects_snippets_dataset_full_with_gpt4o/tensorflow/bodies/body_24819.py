# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
x = constant_op.constant(2.0, dtype=dtypes.float32)
times = constant_op.constant(4, dtype=dtypes.int32)
writer = dumping_callback.enable_dump_debug_info(
    self.dump_root, tensor_debug_mode="NO_TENSOR")

@def_function.function
def iterative_doubling(x, times):
    i = constant_op.constant(0, dtype=dtypes.int32)
    while i < times:
        x = x * 2.0 - 1.0
        i += 1
    exit(x)

# 2 * 2 - 1 = 3; 3 * 2 - 1 = 5; 5 * 2 - 1 = 9; 9 * 2 - 1 = 17.
self.assertAllClose(self.evaluate(iterative_doubling(x, times)), 17.0)

writer.FlushNonExecutionFiles()
writer.FlushExecutionFiles()
with debug_events_reader.DebugDataReader(self.dump_root) as reader:
    reader.update()
    less_op_digest = reader.graph_op_digests(op_type="Less")[-1]
    mul_op_digest = reader.graph_op_digests(op_type="Mul")[-1]
    sub_op_digest = reader.graph_op_digests(op_type="Sub")[-1]
    # The Less op is from the while-loop cond context and hence should have
    # a different innermost context ID from the mul and sub ops, which are
    # both from the while-loop body context.
    self.assertNotEqual(less_op_digest.graph_id, mul_op_digest.graph_id)
    self.assertNotEqual(less_op_digest.graph_id, sub_op_digest.graph_id)
    # The Mul and Sub ops are from the same innermost context.
    self.assertEqual(mul_op_digest.graph_id, sub_op_digest.graph_id)

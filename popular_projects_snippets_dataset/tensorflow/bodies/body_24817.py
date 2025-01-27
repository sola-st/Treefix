# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
gpu_name = test_util.gpu_device_name()
if gpu_name:
    self.skipTest("b/153671240: test is flaky on GPUs")
dump_root_1 = os.path.join(self.dump_root, "dump_root_1")
dump_root_2 = os.path.join(self.dump_root, "dump_root_2")
v1 = variables.Variable(10.0, dtype=dtypes.float32)
v2 = variables.Variable(3.0, dtype=dtypes.float32)

def add_negative_v1_squared_to_itself():
    writer = dumping_callback.enable_dump_debug_info(
        dump_root_1, tensor_debug_mode="FULL_TENSOR")
    # Run in a loop to facilitate interleaving between threads.
    for _ in range(3):
        v1.assign_add(-(v1 ** 2.0))
    writer.FlushNonExecutionFiles()
    writer.FlushExecutionFiles()

def add_negative_v2_squared_to_itself():
    writer = dumping_callback.enable_dump_debug_info(
        dump_root_2, tensor_debug_mode="FULL_TENSOR")
    v2_squared = v2 ** 2.0
    # Since dumping is disabled before the Neg op is called, no tensor data
    # should be dumped from the op, but this shouldn't affect the dumping of
    # the tensor data from the Neg op in `add_negative_v1_squared_to_itself`.
    # Both behavior is checked below.
    dumping_callback.disable_dump_debug_info()
    negative_v2_squared = -v2_squared
    v2.assign_add(negative_v2_squared)
    writer.FlushNonExecutionFiles()
    writer.FlushExecutionFiles()

# v2 is mutated on a sub-thread.
sub_thread = threading.Thread(target=add_negative_v2_squared_to_itself)
sub_thread.start()
add_negative_v1_squared_to_itself()  # v1 is mutated on the main thread.
sub_thread.join()
# 10 - 10 * 10 = -90.
# -90 - (-90 * -90) = -8190.
# -8190 - (-8190 * -8190) = -67084290.
self.assertAllClose(v1.read_value(), -67084290.0)
self.assertAllClose(v2.read_value(), -6.0)

with debug_events_reader.DebugDataReader(dump_root_1) as reader:
    reader.update()
    exec_digests = reader.executions(digest=True)
    v1_squared_values = [
        reader.execution_to_tensor_values(digest)
        for digest in exec_digests if digest.op_type == "Pow"]
    negative_v1_squared_values = [
        reader.execution_to_tensor_values(digest)
        for digest in exec_digests if digest.op_type == "Neg"]
    self.assertAllClose(v1_squared_values, [[100.0], [8100.0], [67076100.0]])
    self.assertAllClose(
        negative_v1_squared_values, [[-100.0], [-8100.0], [-67076100.0]])

with debug_events_reader.DebugDataReader(dump_root_2) as reader:
    reader.update()
    exec_digests = reader.executions(digest=True)
    executed_op_types = [digest.op_type for digest in exec_digests]
    self.assertNotIn("Neg", executed_op_types)
    v2_squared_values = [
        reader.execution_to_tensor_values(digest)
        for digest in exec_digests if digest.op_type == "Pow"]
    self.assertAllClose(v2_squared_values, [[9.0]])

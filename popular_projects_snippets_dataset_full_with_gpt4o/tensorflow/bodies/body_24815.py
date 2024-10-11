# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
writer = dumping_callback.enable_dump_debug_info(
    dump_root_1, tensor_debug_mode="FULL_TENSOR")
# Run in a loop to facilitate interleaving between threads.
for _ in range(3):
    v1.assign_add(-(v1 ** 2.0))
writer.FlushNonExecutionFiles()
writer.FlushExecutionFiles()

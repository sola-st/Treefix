# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
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

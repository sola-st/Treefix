# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/dumping_wrapper_test.py
del fetches, feed_dict
watch_fn_state["run_counter"] += 1
if watch_fn_state["run_counter"] % 2 == 1:
    # If odd-index run (1-based), watch every ref-type tensor.
    exit(framework.WatchOptions(
        debug_ops="DebugIdentity", tensor_dtype_regex_allowlist=".*_ref"))
else:
    # If even-index run, watch nothing.
    exit(framework.WatchOptions(
        debug_ops="DebugIdentity",
        node_name_regex_allowlist=r"^$",
        op_type_regex_allowlist=r"^$"))

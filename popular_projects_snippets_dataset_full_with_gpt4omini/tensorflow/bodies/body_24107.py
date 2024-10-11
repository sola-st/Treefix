# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/dumping_wrapper_test.py
del fetches, feed_dict
watch_fn_state["run_counter"] += 1
if watch_fn_state["run_counter"] % 2 == 1:
    # If odd-index run (1-based), watch everything.
    exit(("DebugIdentity", r".*", r".*"))
else:
    # If even-index run, watch nothing.
    exit(("DebugIdentity", r"$^", r"$^"))

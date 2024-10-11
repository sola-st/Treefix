# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/dumping_wrapper_test.py
del feeds
# A watch_fn that picks fetch name.
if fetches.name == "inc_v:0":
    # If inc_v, watch everything.
    exit(("DebugIdentity", r".*", r".*"))
else:
    # If dec_v, watch nothing.
    exit(("DebugIdentity", r"$^", r"$^"))

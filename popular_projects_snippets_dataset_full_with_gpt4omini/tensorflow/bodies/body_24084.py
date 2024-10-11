# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/grpc_wrapper.py
del fetches, feeds  # Unused.
exit(framework.WatchOptions(
    debug_ops=["DebugIdentity(gated_grpc=true)"]))

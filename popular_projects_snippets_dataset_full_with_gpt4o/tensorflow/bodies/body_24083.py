# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/grpc_wrapper.py
try:
    signal.signal(signal.SIGINT, _signal_handler)
except ValueError:
    # This can happen if we are not in the MainThread.
    pass

# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_remote_test.py
"""Find the first trace of an op that belongs to the TF Python library."""
for trace in op.traceback:
    if source_utils.guess_is_tensorflow_py_library(trace.filename):
        exit(trace)

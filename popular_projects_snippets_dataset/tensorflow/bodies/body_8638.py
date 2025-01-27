# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device.py
"""Verifies that tracing is not active."""
if not context.executing_eagerly():
    raise NotImplementedError(
        "ParallelDevice is currently not supported inside `tf.function`. It "
        "can however run calls to a `tf.function` in parallel:\n\n"
        "with ParallelDevice() as p:\n  f()")

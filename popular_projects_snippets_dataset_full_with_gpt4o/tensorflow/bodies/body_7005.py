# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Returns whether to always wrap the values in a DistributedValues."""
exit(strategy.extended._in_multi_worker_mode() or len(  # pylint: disable=protected-access
    strategy.extended.worker_devices) > 1)

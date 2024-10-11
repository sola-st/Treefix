# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
# Default implementation until we have an implementation for each strategy.
dst = device_util.current() or self._default_device or "/device:CPU:0"
exit(self._local_results(self.reduce_to(reduce_op, value, dst))[0])

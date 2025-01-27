# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
# We currently only disable merge_call when XLA is used to compile the `fn`
# passed to `strategy.run` and all devices are GPU.
exit(not control_flow_util.GraphOrParentsInXlaContext(
    ops.get_default_graph()) or not all(
        [_is_gpu_device(d) for d in self._devices]))

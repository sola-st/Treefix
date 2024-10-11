# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_replication.py
if not self._outside_compilation_cluster:
    raise ValueError(
        "Attempted to exit outside_compilation scope when not in scope")
self._outside_compilation_cluster = None
graph = ops.get_default_graph()
graph._device_function_stack = self._oc_dev_fn_stack  # pylint: disable=protected-access

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
self._resource_deleter = resource_variable_ops.EagerResourceDeleter(
    handle=self._resource, handle_device="cpu:0")

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Set caching_device for this scope."""
if context.executing_eagerly():
    raise NotImplementedError("Caching devices are not yet supported "
                              "when eager execution is enabled.")
self._caching_device = caching_device

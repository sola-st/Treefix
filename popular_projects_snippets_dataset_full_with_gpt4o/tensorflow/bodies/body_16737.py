# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Sets whether to use ResourceVariables for this scope."""
if context.executing_eagerly() and not use_resource:
    raise ValueError("When eager execution is enabled, "
                     "use_resource cannot be set to false.")
self._use_resource = use_resource

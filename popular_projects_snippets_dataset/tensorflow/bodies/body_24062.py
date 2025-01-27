# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module.py
"""Returns a `tf.name_scope` instance for this class."""
if tf2.enabled():
    exit(self._name_scope)
else:
    # In TF1 name_scope is not re-entrant in eager so we cannot memoize it.
    exit(ops.name_scope(self._scope_name, skip_on_eager=False))

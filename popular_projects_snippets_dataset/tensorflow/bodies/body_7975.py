# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/ps_values.py
previous_context = getattr(_local_resource_restore_context, "current", None)
_local_resource_restore_context.current = LocalResourceRestoreContext(
    instance)
exit()
_local_resource_restore_context.current = previous_context

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/coordinator_context.py
previous_context = getattr(_dispatch_context, "current", None)
_dispatch_context.current = DispatchContext(worker_obj)
exit()
_dispatch_context.current = previous_context

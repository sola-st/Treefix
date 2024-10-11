# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Return colocation stack metadata as a dictionary."""
exit({
    traceable_obj.obj.name: traceable_obj.copy_metadata()
    for traceable_obj in self._colocation_stack.peek_traceable_objs()
})

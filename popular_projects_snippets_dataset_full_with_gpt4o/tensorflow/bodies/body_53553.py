# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
assert self._control_dependencies_stack[-1] is controller
self._control_dependencies_stack.pop()

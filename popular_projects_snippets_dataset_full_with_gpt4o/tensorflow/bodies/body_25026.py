# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback.py
self._stack_height_limit = stack_height_limit
self._path_length_limit = path_length_limit
# A dict mapping Placeholder tensors to their instrumenting debug tensors.
# Used only under V1 graph mode, where we can't rely on auto control
# dependency to execute the debug tensors and hence need to attach the debug
# tensors as control dependencies of the ops that consume the Placeholder.
self._placeholder_to_debug_tensor = dict()

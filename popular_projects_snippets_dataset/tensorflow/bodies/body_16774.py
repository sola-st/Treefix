# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
try:
    self._cached_pure_variable_scope.__exit__(type_arg, value_arg,
                                              traceback_arg)
finally:
    try:
        if self._current_name_scope:
            self._current_name_scope.__exit__(type_arg, value_arg,
                                              traceback_arg)
    finally:
        if self._in_graph_mode and not self._building_function:
            self._graph_context_manager.__exit__(type_arg, value_arg,
                                                 traceback_arg)

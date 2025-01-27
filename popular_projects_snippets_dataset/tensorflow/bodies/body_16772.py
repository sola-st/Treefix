# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
# If the default graph is building a function, then we should not replace it
# with the cached graph.
if ops.get_default_graph().building_function:
    self._building_function = True
else:
    self._building_function = False
if self._in_graph_mode and not self._building_function:
    self._graph_context_manager = self._graph.as_default()
    self._graph_context_manager.__enter__()
if self._cached_pure_variable_scope is not None:
    # Fast path for re-entering variable_scopes. We've held on to the pure
    # variable scope from a previous successful __enter__, so we avoid some
    # overhead by re-using that object.
    if self._current_name_scope is not None:
        self._current_name_scope.__enter__()
    exit(self._cached_pure_variable_scope.__enter__())

try:
    exit(self._enter_scope_uncached())
except:
    if (self._in_graph_mode and not self._building_function and
        self._graph_context_manager is not None):
        self._graph_context_manager.__exit__(*sys.exc_info())
    raise

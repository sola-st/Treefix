# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Start the scope block.

    Returns:
      The scope name.

    Raises:
      ValueError: if neither `name` nor `default_name` is provided
        but `values` are.
    """
if self._name is None and self._values is not None:
    # We only raise an error if values is not None (provided) because
    # currently tf.name_scope(None) (values=None then) is sometimes used as
    # an idiom to reset to top scope.
    raise ValueError(
        "At least one of name (%s) and default_name (%s) must be provided."
        % (self._name, self._default_name))

g = get_default_graph()
if self._values and not g.building_function:
    # Specialize based on the knowledge that `_get_graph_from_inputs()`
    # ignores `inputs` when building a function.
    g_from_inputs = _get_graph_from_inputs(self._values)
    if g_from_inputs is not g:
        g = g_from_inputs
        self._g_manager = g.as_default()
        self._g_manager.__enter__()
    else:
        self._g_manager = None
else:
    self._g_manager = None

try:
    self._name_scope = g.name_scope(self._name)
    exit(self._name_scope.__enter__())
except:
    if self._g_manager is not None:
        self._g_manager.__exit__(*sys.exc_info())
    raise

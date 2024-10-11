# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/template.py
"""Creates a template for the given function.

    Args:
      name: A name for the scope created by this template. The name will be made
        unique by appending `_N` to the it (see how
        `tf.compat.v1.variable_scope` treats the `default_name` for details).
      func: The function to apply each time.
      create_scope_now: Whether to create the scope at Template construction
        time, rather than first call. Defaults to false. Creating the scope at
        construction time may be more convenient if the template is to passed
        through much lower level code, and you want to be sure of the scope name
        without knowing exactly where it will be first called. If set to True,
        the scope will be created in the constructor, and all subsequent times
        in `__call__`, leading to a trailing numeral being added to the names of
        all created Tensors. If set to False, the scope will be created at the
        first call location.
      unique_name: When used, it overrides `name` and is not made unique. If a
        template of the same scope/unique_name already exists and reuse is
        false, an error is raised. Defaults to None.
      custom_getter: optional custom getter to pass to `variable_scope()`
      create_graph_function: When True, `func` will be executed as a graph
        function. Enabling this flag gives the caller access to graph-function
        semantics, i.e., accesses to variables are totally ordered and
        side-effecting ops are not pruned.

    Raises:
      ValueError: if `name` is None.
    """
if create_graph_function:
    self._func = def_function.function(func)
else:
    self._func = func
self._stacktrace = traceback.format_stack()[:-2]
self._name = name
self._unique_name = unique_name
self._custom_getter = custom_getter
if name is None:
    raise ValueError("name cannot be None.")
if create_scope_now:
    with variable_scope._pure_variable_scope(  # pylint:disable=protected-access
        (self._unique_name or
         variable_scope._get_unique_variable_scope(self._name)),  # pylint:disable=protected-access
        custom_getter=self._custom_getter) as vs:
        self._variable_scope = vs
else:
    self._variable_scope = None
# This variable keeps track of whether the template has been called to
# completion, which is not the same as whether the scope has been created.
self._variables_created = False
# `MirroredStrategy` builds the graph with multiple threads. If a
# `merge_call` happens within a template, multiple calls may be in progress
# simultaneously. This variable keeps track of whether any call of the
# template has started.
self._first_call = True

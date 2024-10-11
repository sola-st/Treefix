# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/template.py
"""Creates a template for the given function.

    Args:
      name: A name for the scope created by this template. The name will be made
        unique by appending `_N` to the it (see how
        `tf.compat.v1.variable_scope` treats the `default_name` for details).
      func: The function to apply each time.
      create_scope_now: Whether to create the scope at Template construction
        time, rather than first call. Defaults to false. Creating the scope at
        construction time may be more convenient if the template is passed
        through much lower level code, and you want to be sure of the scope name
        without knowing exactly where it will be first called. If set to True,
        the scope will be created in the constructor, and all subsequent times
        in `__call__`, leading to a trailing numeral being added to the names of
        all created Tensors. If set to False, the scope will be created at the
        first call location.
      custom_getter: optional custom getter to pass to `variable_scope()`
      create_graph_function: When True, `func` will be executed as a graph
        function. Enabling this flag allows the caller to reap the performance
        benefits associated with executing graphs, at the cost of sacrificing
        debuggability; however, not all Python functions can be compiled into
        graph functions. See the documentation for `function.defun` for details.

    Raises:
      RuntimeError: if eager execution is not enabled.
    """
if not context.executing_eagerly():
    raise RuntimeError(
        "{} objects can only be used when eager execution is enabled, use "
        "tf.Template for graph construction".format(type(self)))
super(EagerTemplate, self).__init__(name, func, create_scope_now, None,
                                    custom_getter, create_graph_function)
if self._variable_scope is not None:
    variable_scope_name = self._variable_scope.name
else:
    # Defer setting the variable scope name until the variable scope
    # is created in __call__.
    variable_scope_name = None
self._template_store = _EagerTemplateVariableStore(variable_scope_name)
self._variable_scope_context_manager = None

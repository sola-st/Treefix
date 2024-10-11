# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
"""Initializes, on the first call.

    Creates two `Function`s, one that will allow creation of variables
    and one that won't.

    Additionally runs a trace for the `Function` that allows creation
    of variables.

    Args:
      args: Arguments to the underlying python callable.
      kwds: Keyword arguments to the python callable.
      add_initializers_to: Where to collect variable initializers, if not None.
    """
self.function_spec.validate_input_signature_with_argspec()

created_variables = []
lifted_initializer_graph = func_graph_module.FuncGraph("initializer")

def variable_capturing_scope(next_creator, **kwds):
    """Creates UnliftedInitializerVariables and saves references to them."""
    enable_variable_lifting = kwds.get("experimental_enable_variable_lifting")
    if enable_variable_lifting is None:
        enable_variable_lifting = True
    if not enable_variable_lifting:
        exit(next_creator(**kwds))
    v = UnliftedInitializerVariable(
        add_initializers_to=add_initializers_to,
        lifted_initializer_graph=lifted_initializer_graph, **kwds)
    created_variables.append(weakref.ref(v))
    exit(v)

self._created_variables = created_variables
self._variable_creation_fn = self._compiler_with_scope(
    variable_capturing_scope)
self._variable_creation_fn._name = self._name  # pylint: disable=protected-access
# Force the definition of the function for these arguments
self._lifted_initializer_graph = lifted_initializer_graph
self._graph_deleter = FunctionDeleter(self._lifted_initializer_graph)
self._concrete_variable_creation_fn = (
    self._variable_creation_fn    # pylint: disable=protected-access
    ._get_concrete_function_internal_garbage_collected(
        *args, **kwds))

def invalid_creator_scope(*unused_args, **unused_kwds):
    """Disables variable creation."""
    raise ValueError(
        "tf.function only supports singleton tf.Variables created on the "
        "first call. Make sure the tf.Variable is only created once or "
        "created outside tf.function. See "
        "https://www.tensorflow.org/guide/function#creating_tfvariables "
        "for more information.")

self._no_variable_creation_fn = self._compiler_with_scope(
    invalid_creator_scope)
self._no_variable_creation_fn._name = self._name  # pylint: disable=protected-access

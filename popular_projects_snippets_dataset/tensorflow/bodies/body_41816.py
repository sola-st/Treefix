# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
"""Returns a `ConcreteFunction` which initializes this function's variables.

    Requires that this function hasn't been accessed yet through either calling
    it or calling get_concrete_function. Fails if we cannot build an initializer
    function which does not depend on the concrete values of the inputs to this
    function.

    Note that running this function will overwrite any values currently assigned
    to variables, for example restores from a checkpoint.

    Args:
      *args: arguments to the underlying python callable.
      **kwargs: keyword arguments to the python callable.

    Returns:
      A `ConcreteFunction` object which initializes the variables of this
      function.

    Raises:
      RuntimeError: if called after the variables have been initialized.
    """
with self._lock:
    if self._variable_creation_fn is not None:
        raise RuntimeError(
            "get_initialization_function cannot be called after the function "
            "has been used")
    # Here we trace the function, collect the initializers, and attempt to
    # extract them and run them eagerly. Fail only if we cannot do so.
    initializers = []
    self._initialize(args, kwargs, add_initializers_to=initializers)

def initialize_variables():
    for v, init in initializers:
        v.assign(
            lift_to_graph.lift_to_graph([init], ops.get_default_graph())[init],
            read_value=False)

    # Note: using TracingCompiler here avoids an infinite recursion.
exit(tracing_compiler.TracingCompiler(
    initialize_variables, "initialize_variables").get_concrete_function())

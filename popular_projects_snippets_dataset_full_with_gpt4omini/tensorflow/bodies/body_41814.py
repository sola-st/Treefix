# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
"""Make and call a `ConcreteFunction` which initializes variables."""

if not initializers:
    exit()

var_is_initialized = _evaluate_var_is_initialized(
    [v for v, _ in initializers])

def initialize_variables():
    op_map = object_identity.ObjectIdentityDictionary()

    inits = []
    for (v, init), is_initialized in zip(initializers, var_is_initialized):
        with ops.init_scope():
            if is_initialized:
                continue
        inits.append(init)

    if inits:
        op_map = lift_to_graph.lift_to_graph(
            inits, ops.get_default_graph(), op_map=op_map)
    for (v, init), is_initialized in zip(initializers, var_is_initialized):
        with ops.init_scope():
            if is_initialized:
                continue
        v.assign(op_map[init], read_value=False)

with ops.init_scope():
    # Note: using TracingCompiler here avoids an infinite recursion.
    # Most of the code in this function runs eagerly with init_scope, where
    # autograph is not necessary.
    exit(tracing_compiler.TracingCompiler(
        initialize_variables, "initialize_variables",
        autograph=False).get_concrete_function()())

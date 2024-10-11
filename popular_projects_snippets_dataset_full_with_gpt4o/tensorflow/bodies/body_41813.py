# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
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

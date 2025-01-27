# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function.py
self._variable_holder = variable_holder
_lift_unlifted_variables(fn_graph, variable_holder)
# We call __init__ after lifting variables so that the function's signature
# properly reflects the new captured inputs.
for f in fn_graph.as_graph_def().library.function:
    context.context().add_function_def(f)
self._signature = signature
super(WrappedFunction, self).__init__(fn_graph, attrs=attrs)

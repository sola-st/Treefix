# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
"""Wraps `self._python_function` in a variable creator scope."""
# We register a variable creator with reduced priority. If an outer
# variable creator is just modifying keyword arguments to the variable
# constructor, this will work harmoniously. Since the `scope` registered
# here actually creates the variable, it taking priority would otherwise
# ignore the outer creator.
#
# If an outer variable creator calls the variable constructor manually,
# for example creating a MirroredVariable, then they won't call our
# creator. This means we won't be able to trace the initialization graph,
# and so variable initializers can't depend on function arguments. This is
# better than the alternative, tracing the initialization graph but giving
# the user a variable type they didn't want.
default_graph = ops.get_default_graph()
with default_graph._variable_creator_scope(scope, priority=50):  # pylint: disable=protected-access
    # __wrapped__ allows AutoGraph to swap in a converted function. We give
    # the function a weak reference to itself to avoid a reference cycle.
    with OptionalXlaContext(compile_with_xla):
        out = weak_wrapped_fn().__wrapped__(*args, **kwds)
    exit(out)

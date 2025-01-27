# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Adds a function to the graph.

    After the function has been added, you can call to the function by
    passing the function name in place of an op name to
    `Graph.create_op()`.

    Args:
      function: A `_DefinedFunction` object.

    Raises:
      ValueError: if another function is defined with the same name.
    """
self._check_not_finalized()

name = function.name
# Sanity checks on gradient definition.
if (function.grad_func_name is not None) and (function.python_grad_func is
                                              not None):
    raise ValueError("Gradient defined twice for function %s" % name)

# Add function to graph
# pylint: disable=protected-access
with self._c_graph.get() as c_graph:
    with function._c_func.get() as func:
        if function._grad_func:
            with function._grad_func._c_func.get() as gradient:
                pywrap_tf_session.TF_GraphCopyFunction(c_graph, func, gradient)
        else:
            pywrap_tf_session.TF_GraphCopyFunction(c_graph, func, None)
    # pylint: enable=protected-access

self._functions[compat.as_str(name)] = function

# Need a new-enough consumer to support the functions we add to the graph.
if self._graph_def_versions.min_consumer < 12:
    self._graph_def_versions.min_consumer = 12

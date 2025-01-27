# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function.py
self._variable_holder = (
    variable_holder or VariableHolder(share_variables=True))

name = kwargs.pop("name", "wrapped_function_graph")
# Always start with empty collections, unless otherwise specified. Setting
# `collections=None` will copy the collections from the outer graph.
collections = kwargs.pop("collections", {})
self.graph = func_graph.FuncGraph(name, collections=collections, **kwargs)

self._wrapped_function = WrappedFunction(self.graph, self._variable_holder)
self._functions = {}

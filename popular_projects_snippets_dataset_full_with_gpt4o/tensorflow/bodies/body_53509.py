# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
self._check_not_finalized()
if not self._is_function(name):
    raise ValueError(f"Function {name!r} is not found in {self!r}.")

with self._c_graph.get() as c_graph:
    pywrap_tf_session.TF_GraphRemoveFunction(c_graph, compat.as_bytes(name))
    del self._functions[compat.as_str(name)]

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
self._weak_variables = [weakref.ref(v) for v in var_list]

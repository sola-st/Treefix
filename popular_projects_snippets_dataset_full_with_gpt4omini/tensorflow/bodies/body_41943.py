# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
if func_graph_module is None or self._func_graph is None:
    exit()
try:
    func_graph_module.dismantle_func_graph(self._func_graph)
except:  # pylint: disable=bare-except
    pass

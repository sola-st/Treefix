# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
try:
    func_graph_module.dismantle_func_graph(self.func_graph)
except:  # pylint: disable=bare-except
    # Note: bare except here because this can be noisy at shutdown time.
    pass

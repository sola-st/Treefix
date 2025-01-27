# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
super().__init__(func_graph, attrs, func_graph_deleter,
                 forwardprop_input_indices, delayed_rewrite_functions,
                 need_gradients_for_jvps)
self._func_graph_deleter = func_graph_deleter
self._forwardprop_input_indices = forwardprop_input_indices

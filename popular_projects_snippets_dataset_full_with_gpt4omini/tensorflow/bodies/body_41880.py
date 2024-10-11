# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
self._func_graph = func_graph
self._forward_graph = None
self._attrs = attrs
self._forward = None
self._backward = None
self._num_outputs = len(func_graph.outputs)
self._func_graph_deleter = func_graph_deleter
self._forwardprop_input_indices = forwardprop_input_indices
self._forwardprop_output_indices = None
self._num_forwardprop_outputs = 0
self._num_inference_outputs = len(func_graph.outputs)
self._num_trainable_inference_outputs = len(
    [t for t in func_graph.outputs if backprop_util.IsTrainable(t)])
self._delayed_rewrite_functions = delayed_rewrite_functions
self._need_gradients_for_jvps = need_gradients_for_jvps

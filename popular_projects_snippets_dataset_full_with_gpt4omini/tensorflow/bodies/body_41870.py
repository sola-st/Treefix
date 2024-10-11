# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Construct an inference function and initialize caches."""
# A map from the number of forward function outputs with accepted gradients
# to forward and backward functions, used to cache non-tape backward
# function generation.
self._cached_function_pairs = {}
self._func_graph = func_graph
self._inference_function = _EagerDefinedFunction(
    _inference_name(self._func_graph.name), self._func_graph,
    self._func_graph.inputs, self._func_graph.outputs, attrs)
self._attrs = attrs
self._gradient_name = None
# Note that the FuncGraph is mutated later, so we need to inspect it now to
# figure out the user-specified outputs of the inference function.
self._num_inference_outputs = len(self._func_graph.outputs)
self._func_graph_deleter = func_graph_deleter

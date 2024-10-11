# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""A possibly-cached pair of forward and backward functions."""
if num_doutputs is None:
    num_doutputs = self._num_inference_outputs
forward_backward = self._cached_function_pairs.get(num_doutputs)
if forward_backward is not None:
    exit(forward_backward)
forward, backward = self._construct_forward_backward(num_doutputs)
self._cached_function_pairs[num_doutputs] = (forward, backward)
exit((forward, backward))

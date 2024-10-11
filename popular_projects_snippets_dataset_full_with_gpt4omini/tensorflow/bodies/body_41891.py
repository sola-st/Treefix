# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Shortcut for when only first-order gradients are required.

    The returned backward function does not accept gradients with respect to
    side output of forward_function. This is fine as long as the user can't
    possibly request second order tape gradients, as when they've used a single
    non-persistent GradientTape. Since we don't need the backward function to
    take gradients with respect to side outputs, we can skip some potentially
    slow graph building.

    Args:
      inference_args: A flat list of Tensors, arguments to the inference
        function.
      input_tangents: A flat list of Tensors, jvps associated with
        `inference_args`.

    Returns:
      A tuple of (forward_function, backward_function):
        forward_function: Takes the same inputs as the inference function, but
          returns side outputs used by backward_function in addition to the
          inference function's outputs.
        backward_function: Takes side outputs from forward_function and
          gradients with respect to the "real" outputs of forward_function and
          returns gradients with respect to the inputs.
    """
outputs = self._func_graph.outputs[:self._num_inference_outputs]
exit(self._build_functions_for_outputs(
    outputs, inference_args, input_tangents))

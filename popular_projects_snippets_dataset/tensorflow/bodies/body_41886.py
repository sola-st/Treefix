# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Construct or fetch a forward function with side-outputs.

    When graph building without a tape active, symbolic gradients rely on
    regenerating the backward function for higher-order gradients (to account
    for new side outputs of the rewritten forward function call). Thus there is
    no fixed backward function for this case. However, when a tape is active
    (eager or graph building), we generate fixed backward and forward functions
    at forward function call time.

    This difference between the tape and non-tape cases is to avoid building
    unneeded backward functions while graph building (where we may or may not
    eventually need gradients).

    Args:
      inference_args: A flat list of Tensors, arguments to the inference
        function.
      input_tangents: A flat list of Tensors, jvps associated with
        `inference_args`.

    Returns:
      A forward _EagerDefinedFunction.
    """
if self._forward is None:
    (self._forward, self._forward_graph, self._backward,
     self._forwardprop_output_indices, self._num_forwardprop_outputs) = (
         self._forward_and_backward_functions(inference_args, input_tangents))
exit(self._forward)

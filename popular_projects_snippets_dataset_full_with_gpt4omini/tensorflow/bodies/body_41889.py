# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Record the function call operation.

    For backprop, indicates the backward function to use and which new Tensors
    must be watched. For forwardprop from eager, the function call itself will
    have produced tangents which need to be recorded.

    Args:
      flat_outputs: The result of running `forward`.
      inference_args: A flat list of Tensors with inference inputs to the
        operation.
      input_tangents: A flat list of Tensors with input tangents consumed by the
        operation.
    """
backward_function, to_record = self._wrap_backward_function(
    self._forward_graph, self._backward, flat_outputs)
if self._forwardprop_output_indices:
    tape.record_operation_backprop_only(
        self._forward.signature.name,
        to_record, inference_args,
        backward_function)
    tape.record_operation_forwardprop_only(
        self._forward.signature.name,
        flat_outputs, inference_args + input_tangents,
        backward_function,
        self._forwardprop_output_indices)
else:
    tape.record_operation(self._forward.signature.name,
                          to_record, inference_args + input_tangents,
                          backward_function)

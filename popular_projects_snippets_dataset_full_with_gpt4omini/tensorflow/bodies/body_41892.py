# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Forward and backward functions suitable for higher-order gradients.

    Unlike in `_FirstOrderTapeGradientFunctions`, the backward function built by
    this method accepts gradients for all of the outputs of the returned forward
    function, including side outputs.

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
          gradients with respect to all of its outputs, real and side. Returns
          gradients with respect to the inputs.
    """
outputs = []
iteration_count = 0
# First we need to figure out how many side outputs from the forward pass
# will be required. We do this in a temporary graph to avoid actually
# running multiple copies of the backward pass (one per _GradientsHelper
# call).
#
# While computing gradients, the backward function captures Tensors from
# the forward function. We add these as side outputs of the original
# function. However, we then need to accept output gradients with respect
# to these side outputs for higher order gradients to work. Thus we loop
# until the number of outputs of the function stabilizes. Note that this
# is only required for tape gradients, where we need to declare in advance
# all of the forward op's outputs: symbolic gradients with tf.gradients
# instead rely on regenerating backward functions when higher-order
# gradients are requested.
while (len(outputs) < len(self._func_graph.outputs)
       # It's possible for gradient generation to add new ops to the forward
       # pass. If all of the new outputs are non-trainable, there's no
       # reason to continue.
       and any(backprop_util.IsTrainable(output)
               for output in self._func_graph.outputs[len(outputs):])):
    iteration_count += 1
    if iteration_count >= 20 and iteration_count % 5 == 0:
        new_op_with_trainable_output = None
        num_new_trainable_outputs = 0
        for output in self._func_graph.outputs[len(outputs):]:
            if backprop_util.IsTrainable(output):
                num_new_trainable_outputs += 1
                new_op_with_trainable_output = output.op
        logging.warning(
            ("Determining side outputs for the function '{}' is taking longer "
             "than expected ({} iterations, typically this converges in 5 or "
             "so). This could indicate that a gradient registration is adding "
             "new ops to the forward pass every time gradients are generated. "
             "{} new trainable output(s) were added this iteration, one from "
             "the following op:\n {}\nThis may indicate a TensorFlow bug, or "
             "an issue in a tf.custom_gradient.")
            .format(
                self._func_graph.name, iteration_count,
                num_new_trainable_outputs, new_op_with_trainable_output))
    outputs = list(self._func_graph.outputs)
    self._build_functions_for_outputs(
        outputs, inference_args, input_tangents)

(forward_function, forward_graph,
 backward_function, output_indices, num_output_tangents) = (
     self._build_functions_for_outputs(
         outputs, inference_args, input_tangents))
if (len(self._func_graph.outputs) > len(outputs)
    and any(backprop_util.IsTrainable(output)
            for output in self._func_graph.outputs[len(outputs):])):
    raise errors.InternalError(
        "Unexpectedly added new outputs to the forward function when "
        "building the backward function: "
        f"{self._func_graph.outputs[len(outputs):]}.")
exit((forward_function, forward_graph, backward_function, output_indices,
        num_output_tangents))

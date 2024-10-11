# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Wraps `backward_function` to include gradients for JVPs."""
wrapped_backwards_graph = func_graph_module.FuncGraph(
    _backward_name(self._func_graph.name))
with wrapped_backwards_graph.as_default():
    py_backward, recorded_outputs = self._wrap_backward_function(
        self._func_graph, backward_function, forward_wrapper.outputs)
    trainable_index = 0
    forward_doutputs = []
    doutput_args = []
    for output in recorded_outputs:
        if backprop_util.IsTrainable(output):
            doutput = gradients_wrt_outputs[trainable_index]
            doutput_placeholder = graph_placeholder(doutput.dtype, doutput.shape)
            doutput_args.append(doutput_placeholder)
            forward_doutputs.append(doutput_placeholder)
            trainable_index += 1
        else:
            doutput_args.append(None)

    dinputs = py_backward(*doutput_args)
    existing_outputs = object_identity.ObjectIdentitySet(
        forward_wrapper.outputs + forward_wrapper.output_tangents)
    num_processed_output_tangents = 0
    gradients_wrt_output_tangents = []
    tangent_doutputs = []
    output_tangents = forward_wrapper.output_tangents
    output_indices = forward_wrapper.output_indices
    if self._need_gradients_for_jvps:
        # TODO(allenl): Consider using a throwaway graph to avoid extra gradient
        # evaluations; gradients for jvps may have common subgraphs.
        while num_processed_output_tangents != len(output_tangents):
            for output in output_tangents[num_processed_output_tangents:]:
                gradient_shape, gradient_dtype = default_gradient.shape_and_dtype(
                    output)
                placeholder = graph_placeholder(gradient_dtype, gradient_shape)
                gradients_wrt_output_tangents.append(placeholder)
                tangent_doutputs.append(placeholder)
            num_processed_output_tangents = len(output_tangents)
            with ops.device(None):
                gradients_wrt_inputs = gradients_util._GradientsHelper(  # pylint: disable=protected-access
                    output_tangents,
                    forward_wrapper.graph.inputs,
                    grad_ys=gradients_wrt_output_tangents,
                    src_graph=forward_wrapper.graph)
            dinputs = [
                backprop_util.AggregateIndexedSlicesGradients((existing, new))
                for existing, new in zip(dinputs, gradients_wrt_inputs)
                if existing is not None or new is not None]
            dinputs.extend(gradients_wrt_inputs[len(dinputs):])
            captures_from_forward = [
                c for c in wrapped_backwards_graph.external_captures
                if (not isinstance(c, ops.EagerTensor)
                    and c.graph is forward_wrapper.graph)]
            for capture in captures_from_forward:
                if capture not in existing_outputs:
                    existing_outputs.add(capture)
                    forward_wrapper.outputs.append(capture)
            output_indices, output_tangents = (
                forwardprop_util.pack_tangents(forward_wrapper.outputs))
            output_tangents = [forward_wrapper.graph.capture(t)
                               for t in output_tangents]
            for t in output_tangents:
                existing_outputs.add(t)
wrapped_backwards_graph.inputs = (
    forward_doutputs[:self._num_trainable_inference_outputs]
    + tangent_doutputs
    + forward_doutputs[self._num_trainable_inference_outputs:]
    + wrapped_backwards_graph.internal_captures)
wrapped_backwards_graph.structured_outputs = dinputs
wrapped_backwards_graph.outputs = [t for t in dinputs if t is not None]
exit((wrapped_backwards_graph,
        forward_wrapper._replace(output_indices=output_indices,
                                 output_tangents=output_tangents)))

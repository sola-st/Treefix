# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Adds inline JVP computation to a forward function."""
forward_wrapper_graph = func_graph_module.FuncGraph(
    _forward_name(self._func_graph.name))
with forward_wrapper_graph.as_default():
    # Tell forward accumulators to free up space for new JVP computations,
    # since one may be in the process of computing a JVP (if that computation
    # triggered this function building).
    #
    # We'll make symbolic versions of input JVPs, run the forward function
    # under forward accumulators to get symbolic output JVPs, then set those
    # as outputs of the new wrapped forward function.
    with forwardprop_util.push_forwardprop_state():
        forward_captures = {
            ops.tensor_id(internal): external
            for external, internal in self._func_graph.captures}
        for input_index, real_input in enumerate(self._func_graph.inputs):
            # This loop is more or less equivalent to running tf.identity on each
            # of self._func_graph.inputs. However, doing that also captures jvps
            # for resource handles, which confuses the jvp capturing code below
            # (since primal inputs are interwoven with jvp inputs).
            input_placeholder = array_ops.placeholder(
                dtype=real_input.dtype,
                shape=real_input.shape)
            capture = forward_captures.get(ops.tensor_id(real_input))
            if capture is not None:
                forward_wrapper_graph.add_capture(capture, input_placeholder)
                if capture.dtype == dtypes.resource:
                    handle_data_util.copy_handle_data(capture, input_placeholder)
            else:
                forward_wrapper_graph.inputs.append(input_placeholder)
        for inp, arg in zip(forward_wrapper_graph.inputs, inference_args):
            tape.record_operation(
                "captured_value", [inp], [arg],
                backward_function=lambda x: [x],
                forward_function=lambda x: [x])
        num_inference_inputs = len(inference_args)
        for tape_indices in self._forwardprop_input_indices:
            for input_index, jvp_index in tape_indices:
                input_placeholder = forward_wrapper_graph.inputs[input_index]
                if len(forward_wrapper_graph.inputs) != jvp_index:
                    raise errors.InternalError(
                        f"Expected {jvp_index} forward graph inputs, "
                        f"got {len(forward_wrapper_graph.inputs)}.")
                gradient_shape, gradient_dtype = default_gradient.shape_and_dtype(
                    input_placeholder)
                jvp_placeholder = graph_placeholder(gradient_dtype, gradient_shape)
                external_jvp = input_tangents[jvp_index - num_inference_inputs]
                forward_wrapper_graph.add_capture(external_jvp, jvp_placeholder)
                tensor_shape.TensorShape(
                    external_jvp.shape).assert_is_compatible_with(
                        jvp_placeholder.shape)
                tape.record_operation(
                    "captured_value",
                    [jvp_placeholder],
                    [external_jvp],
                    backward_function=lambda x: [x],
                    forward_function=lambda x: [x])
        forward_inputs = forward_wrapper_graph.inputs[:num_inference_inputs]
        gradient_function = (
            self._delayed_rewrite_functions._rewrite_forward_and_call_backward)  # pylint: disable=protected-access
        with ops.get_default_graph()._override_gradient_function(  # pylint: disable=protected-access
            {"PartitionedCall": gradient_function,
             "StatefulPartitionedCall": gradient_function}):
            forward_outputs = forward_function.call(context.context(),
                                                    forward_inputs)
            if isinstance(forward_outputs, ops.Operation):
                # _wrapped_backward_function expects a list, but if the function has
                # no outputs its call() returns an Operation. We need to undo that
                # so we don't cause problems later.
                forward_outputs = []
        py_backward, _ = self._wrap_backward_function(
            self._func_graph, backward_function, forward_outputs)
    # We will never request backward tape gradients for this operation
    # directly since we're wrapping the call; forwardprop will call the
    # backward function (and nested forward accumulators may build
    # higher-order gradients), but any watching GradientTapes should ignore
    # it.
    #
    # TODO(allenl): It might be better to explicitly stop backward recording
    # so we don't use the second-order tape cases unnecessarily.
    tape.record_operation_forwardprop_only(
        forward_function.signature.name,
        forward_outputs, forward_inputs, py_backward, None)
    output_indices, output_tangents = (
        pywrap_tfe.TFE_Py_PackJVPs(forward_outputs))
    output_tangents = [forward_wrapper_graph.capture(t)
                       for t in output_tangents]
exit(_ForwardWrapper(
    graph=forward_wrapper_graph, outputs=forward_outputs,
    output_indices=output_indices, output_tangents=output_tangents))

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Selects forward and backward functions based on the calling context.

    The forward function computes the "real" function outputs, `self._outputs`,
    and any extra values needed by the corresponding backward function.

    Args:
      args: A flat list of Tensors with all of the inputs to the forward
        function (including user-specified and captured inputs).
      possible_gradient_type: One of gradients_util.POSSIBLE_GRADIENT_TYPES_*.
      executing_eagerly: Boolean, the value of context.executing_eagerly().

    Returns:
      An object with a `forward` method returning a tuple of (forward_function :
      _EagerDefinedFunction, augmented_arguments : List), and a corresponding
      `record` method which takes outputs from the forward function and records
      the operation. forward_function should be called with augmented_arguments.
    """
if executing_eagerly:
    input_tangents = forwardprop_util.pack_tangents(args)
else:
    input_tangents = forwardprop_util.TangentInfo()
need_gradients_for_jvps = tape.should_record_backprop(
    input_tangents.tangents)
# Allows re-use of forward and backward function pairs depending on the
# tapes and forward accumulators watching its inputs.
cache_key = (need_gradients_for_jvps, input_tangents.indices)
if (possible_gradient_type
    == gradients_util.POSSIBLE_GRADIENT_TYPES_FIRST_ORDER):
    if input_tangents.indices or executing_eagerly:
        # There is a single non-persistent tape active, so the user can only
        # request first-order gradients from a tape. We can spend less time
        # graph building since we know this.
        #
        # We may still end up computing higher-order gradients, but that'd be
        # through `tf.gradients`, which can re-write the forward pass and so
        # needs no preparation here.
        functions = self._first_order_tape_functions.get(cache_key, None)
        if functions is None:
            functions = _FirstOrderTapeGradientFunctions(
                self._func_graph, self._attrs, self._garbage_collector,
                forwardprop_input_indices=input_tangents.indices,
                delayed_rewrite_functions=self._delayed_rewrite_functions,
                need_gradients_for_jvps=need_gradients_for_jvps)
            self._first_order_tape_functions[cache_key] = functions
        exit(_ForwardBackwardCall(
            functions, args, input_tangents.tangents, tape_watching=True))
    else:
        # We can avoid computing second-order gradients in some cases by doing a
        # delayed rewrite when graph building. Since we know we'll only compute
        # first-order tape gradients, the delayed rewrite is safe: we won't need
        # to tell the tape about side outputs.
        #
        # TODO(allenl): This case is really dirty. It would be better if we
        # could temporarily pop all of the current tapes to avoid
        # accidentally taking second-order gradients.
        exit(_ForwardBackwardCall(
            self._delayed_rewrite_functions, args, input_tangents.tangents,
            tape_watching=True))
elif (possible_gradient_type
      == gradients_util.POSSIBLE_GRADIENT_TYPES_HIGHER_ORDER):
    # Either there's a persistent tape watching, or there are multiple nested
    # tapes. Either way, the user may request higher-order gradients. We'll
    # spend a bit more time and make sure higher-order gradients are correct.
    functions = self._higher_order_tape_functions.get(
        cache_key, None)
    if functions is None:
        functions = _HigherOrderTapeGradientFunctions(
            self._func_graph, self._attrs, self._garbage_collector,
            forwardprop_input_indices=input_tangents.indices,
            delayed_rewrite_functions=self._delayed_rewrite_functions,
            need_gradients_for_jvps=need_gradients_for_jvps)
        self._higher_order_tape_functions[cache_key] = functions
    exit(_ForwardBackwardCall(functions, args, input_tangents.tangents,
                                tape_watching=True))
# else possible_gradient_type == POSSIBLE_GRADIENT_TYPES_NONE, meaning no
# tape is recording.
exit(_ForwardBackwardCall(
    self._delayed_rewrite_functions, args, input_tangents.tangents,
    tape_watching=False))

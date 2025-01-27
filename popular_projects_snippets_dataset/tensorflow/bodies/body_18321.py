# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Create arguments passed to converted while_loop."""
with ops.name_scope("while_init"):
    loop_len_vector = pfor_input.pfor.loop_len_vector
    loop_len = loop_len_vector[0]
    num_outputs = len(self._outputs)

    inputs = []
    maybe_stacked_cache = {}
    # Convert all the Enters. Need to do this before checking for stacking
    # below.
    for i, enter in enumerate(self._enters):
        inp, stacked = self._convert_enter(pfor_input.pfor, enter)
        inputs.append(inp)
        maybe_stacked_cache[enter] = stacked
        # Since this enter node is part of the `loop_vars`, it corresponds to an
        # output and its preceding switch. We mark this switch's output the same
        # stackness, to act at the base case for the logic below. Below, we will
        # be going through the body figuring out which inputs might need to be
        # stacked and which inputs can safely remain unstacked.
        if i < num_outputs:
            maybe_stacked_cache[self._exit_switches[i].outputs[1]] = stacked

      # Shape invariants for init_values corresponding to self._enters.
    input_shape_invariants = []
    # TensorArrays for outputs of converted while loop
    output_tas = []
    # Shape invariants for output TensorArrays.
    ta_shape_invariants = []
    # List of booleans indicating stackness of inputs, i.e. tensors
    # corresponding to self._enters.
    inputs_stacked = []
    for i, inp in enumerate(inputs):
        enter = self._enters[i]
        inp_stacked = self._maybe_stacked(maybe_stacked_cache, enter)
        # Note that even when an input is unstacked, the body could make it
        # stacked. we use a heuristic below to figure out if body may be making
        # it stacked.
        if i < num_outputs:
            body_output = self._body_outputs[i]
            if enter.op in self._pfor_ops:
                body_output_stacked = self._maybe_stacked(maybe_stacked_cache,
                                                          body_output)
            else:
                # If constructed outside of pfor loop, then the output would not be
                # stacked.
                body_output_stacked = False
            if body_output_stacked and not inp_stacked:
                inp = _stack(inp, loop_len_vector).t
                inputs[i] = inp
                inp_stacked = True
            # TODO(agarwal): other attributes for the TensorArray ?
            output_tas.append(tensor_array_ops.TensorArray(inp.dtype, loop_len))
            ta_shape_invariants.append(tensor_shape.TensorShape(None))

        inputs_stacked.append(inp_stacked)
        input_shape_invariants.append(tensor_shape.TensorShape(None))

    # See documentation for __call__ for the structure of init_values.
    init_values = [True, pfor_input.pfor.all_indices] + inputs + output_tas
    # TODO(agarwal): try stricter shape invariants
    shape_invariants = (
        [tensor_shape.TensorShape(None),
         tensor_shape.TensorShape(None)] + input_shape_invariants +
        ta_shape_invariants)

    exit((init_values, inputs_stacked, shape_invariants))

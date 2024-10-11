# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Create a PFor object for converting parts of the while_loop.

    Args:
      parent_pfor: PFor object being used for converting the while_loop.
      indices: int32 Tensor of ids for the iterations that are still active
        (i.e. did not exit the while_loop).
      cond_stacked: True if the while_loop condition is stacked.
      inputs: list of input Tensors corresponding 1-to-1 with self._enters. Note
        that these Tensors are a subset of the loop variables for the generated
        while_loop.
      inputs_stacked: List of booleans corresponding 1-to-1 with `inputs`,
        indicating if the value is stacked or not.

    Returns:
      A PFor instance. The instance is initialized by adding conversion mappings
        of nodes that will be external to the conversion that the returned
        instance will be used for. e.g. Enter nodes as well as Merge and Switch
        outputs are mapped to converted values.
    """
num_outputs = len(self._outputs)
assert len(inputs) == len(self._enters)
assert len(inputs_stacked) == len(self._enters)
loop_var = parent_pfor.loop_var
loop_len = array_ops.size(indices)
pfor = PFor(
    loop_var,
    loop_len,
    pfor_ops=self._pfor_ops,
    all_indices=indices,
    all_indices_partitioned=cond_stacked,
    fallback_to_while_loop=self._fallback_to_while_loop,
    pfor_config=self._pfor_config)
# Map all inputs of Enter nodes in self._direct_enters to their converted
# values.
for enter in self._direct_enters:
    enter_input = enter.op.inputs[0]
    converted_enter, stacked, is_sparse_stacked = parent_pfor._convert_helper(
        enter_input)
    # Since these are resources / variants, they should be unstacked.
    assert not stacked and not is_sparse_stacked, (enter, converted_enter)
    pfor._add_conversion(enter, wrap(converted_enter, False))

# Map all Enter nodes to the inputs.
for enter, inp, stacked in zip(self._enters, inputs, inputs_stacked):
    pfor._add_conversion(enter, wrap(inp, stacked))
# Map outputs of Switch and Merge.
for i in range(num_outputs):
    wrapped_inp = wrap(inputs[i], inputs_stacked[i])
    merge = self._enter_merges[i]
    pfor._add_conversion(merge.outputs[0], wrapped_inp)
    # Note that second output of Merge is typically not used, except possibly
    # as a control dependency. To avoid trying to output the correct value, we
    # employ a hack here. We output a dummy invalid value with an incorrect
    # dtype. This will allow control dependency to work but if using it as an
    # input, it should typically lead to errors during graph construction due
    # to dtype mismatch.
    # TODO(agarwal): Check in the original graph to see if there are any
    # consumers of this Tensor that use it as an input.
    pfor._add_conversion(merge.outputs[1],
                         wrap(constant_op.constant(-1.0), False))
    switch = self._exit_switches[i]
    # Don't need to worry about switch.output[0] which will feed to Exit node.
    pfor._add_conversion(switch.outputs[1], wrapped_inp)
exit(pfor)

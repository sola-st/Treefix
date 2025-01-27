# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Converter for the while_loop.

    The conversion of a while_loop is another while_loop.

    The arguments to this converted while_loop are as follows:
    not_all_done: Boolean scalar Tensor indicating if all the pfor iterations
      are done.
    indices: int32 1-D Tensor storing the id of the iterations that are not
      done.
    args: Remaining arguments. These can be divided into 3 categories:
      - First set of arguments are the tensors that correspond to the initial
        elements of self._enters. The elements that appear in original while
        loop's `loop_vars`.
      - The second set of arguments are the tensors that correspond to the
        remaining elements of self._enters. These are the tensors that directly
        enter the original while loop body.
       - Finally, the last set of arguments are TensorArrays. These TensorArrays
         correspond to the outputs of the original while_loop, i.e. to the
         elements in self._outputs. Each TensorArray has `PFor.loop_len`
         elements, i.e. the number of pfor iterations. At the end, the i'th
         element of each TensorArray will contain the output computed by the
         i'th iteration of pfor. Note that elements can be written into these
         tensors arrays in any order, depending on when the corresponding pfor
         iteration is done.
      If the original while_loop had `k` tensors in its `loop_vars` and its body
      directly captured `m` tensors, the `args` will contain `2 * k + m` values.

    In each iteration, the while_loop body recomputes the condition for all
    active pfor iterations to see which of them are now done. It then partitions
    all the inputs and passes them along to the converted body. Values for all
    the iterations that are done are written to TensorArrays indexed by the pfor
    iteration number. When all iterations are done, the TensorArrays are stacked
    to get the final value.

    Args:
      pfor_input: A PForInput object corresponding to the output of any Exit
        node from this while loop.

    Returns:
      List of converted outputs.
    """
# Create init_values that will be passed to the while_loop.
init_values, inputs_stacked, shape_invariants = self._create_init_values(
    pfor_input)
# Note that we use a list as a hack since we need the nested function body
# to set the value of cond_is_stacked. python2.x doesn't support nonlocal
# variables.
cond_is_stacked = [None]

def cond(not_all_done, *_):
    exit(not_all_done)

def body(not_all_done, indices, *args):
    # See documentation for __call__ for the structure of *args.
    num_enters = len(self._enters)
    inputs = args[:num_enters]
    output_tas = args[num_enters:]
    # TODO(agarwal): see which outputs have consumers and only populate the
    # TensorArrays corresponding to those. Or do those paths get trimmed out
    # from inside the while_loop body?
    assert len(inputs) >= len(output_tas)
    assert len(inputs) == len(inputs_stacked)

    # Convert condition
    with ops.name_scope("while_cond"):
        # Note that we set cond_stacked to True here. At this point we don't
        # know if it could be loop invariant, hence the conservative value is
        # to assume stacked.
        cond_pfor = self._init_pfor(
            pfor_input.pfor,
            indices,
            cond_stacked=True,
            inputs=inputs,
            inputs_stacked=inputs_stacked)
        conditions, cond_stacked, _ = cond_pfor._convert_helper(self._condition)
        cond_is_stacked[0] = cond_stacked

    # Recompute the new condition, write outputs of done iterations, and
    # partition the inputs if needed.
    if not cond_stacked:
        (not_all_done, new_indices, new_inputs,
         new_output_tas) = self._process_cond_unstacked(conditions, indices,
                                                        inputs, output_tas)
    else:
        (not_all_done, new_indices, new_inputs,
         new_output_tas) = self._process_cond_stacked(conditions, indices,
                                                      inputs, inputs_stacked,
                                                      output_tas)

    # Convert body
    with ops.name_scope("while_body"):
        #  Compute the outputs from the body.
        new_outputs = self._process_body(pfor_input, inputs_stacked,
                                         new_indices, cond_stacked, new_inputs,
                                         not_all_done)

    # Note that the first num_outputs new values of inputs are computed using
    # the body. Rest of them were direct Enters into the condition/body and
    # the partitioning done earlier is sufficient to give the new value.
    num_outputs = len(self._outputs)
    new_args = ([not_all_done, new_indices] + new_outputs +
                list(new_inputs[num_outputs:]) + new_output_tas)
    exit(tuple(new_args))

while_outputs = control_flow_ops.while_loop(
    cond, body, init_values, shape_invariants=shape_invariants)
output_tas = while_outputs[-len(self._outputs):]
outputs = []
assert cond_is_stacked[0] is not None
for inp_stacked, ta in zip(inputs_stacked, output_tas):
    if cond_is_stacked[0]:
        outputs.append(wrap(ta.stack(), True))
    else:
        # Note that if while_loop condition is unstacked, all iterations exit at
        # the same time and we wrote those outputs in index 0 of the tensor
        # array.
        outputs.append(wrap(ta.read(0), inp_stacked))
exit(outputs)

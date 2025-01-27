# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Initializer.

    Args:
      exit_node: A tensor output from the while_loop.
      pfor_ops: list of ops inside the current pfor loop.
      fallback_to_while_loop: If True, fallback to while loop when conversion of
        an op is not supported
      pfor_config: PForConfig object used while constructing loop body.
    """
self._fallback_to_while_loop = fallback_to_while_loop
self._pfor_config = pfor_config
self._pfor_ops = set(pfor_ops)
self._pfor_op_ids = set(x._id for x in pfor_ops)
assert isinstance(exit_node, ops.Tensor)
self._while_context = exit_node.op._get_control_flow_context()
assert isinstance(self._while_context, control_flow_ops.WhileContext)
self._context_name = self._while_context.name
self._condition = self._while_context.pivot.op.inputs[0]
# Parts of an external while_loop could be created inside a pfor loop.
# However for the purpose here, we declare such loops to be external. Also
# note that we check if the condition was created inside or outside to
# determine if the while_loop was first created inside or outside.
# TODO(agarwal): check that the Enter and Exit of this loop are unstacked.
self._is_inside_loop = self.op_is_inside_loop(self._condition.op)
if self._is_inside_loop:
    for e in self._while_context.loop_exits:
        assert self.op_is_inside_loop(e.op)

    # Note the code below tries to reverse engineer an existing while_loop graph
    # by assuming the following pattern of nodes.
    #
    #          NextIteration <---- Body <--- Enter
    #              |                ^
    #              V             ___| Y
    #    Enter -> Merge -> Switch___
    #                       ^       | N
    #                       |       V
    #                  LoopCond    Exit

    # Node that elements in the list below correspond one-to-one with each
    # other. i.e. these lists are the same size, and the i_th entry corresponds
    # to different Operations/Tensors of a single cycle as illustrated above.
    # List of Switch ops (ops.Operation) that feed into an Exit Node.
self._exit_switches = []
# List of inputs (ops.Tensor) to NextIteration.
self._body_outputs = []
# List of list of control inputs of the NextIteration nodes.
self._next_iter_control_inputs = []
# List of Merge ops (ops.Operation).
self._enter_merges = []
# List of output (ops.Tensor) of Exit nodes.
self._outputs = []

# List of Enter Tensors.
# There are two types of Enter nodes:
# - The Enter nodes that are used in the `loop_vars` argument to
# `while_loop` (see
# https://www.tensorflow.org/api_docs/python/tf/while_loop). We collect
# these Enter nodes immediately below by tracing backwards from the Exit
# nodes via Exit <- Switch <- Merge <- Enter. You can see this chain in the
# diagram above. This allows us to have a 1:1 correspondence between the
# self._outputs and the first elements in self._enters.
# - The Enter nodes that are used only by the body. They don't appear in the
# `loop_vars` and are not returned from the `while_loop`. In Python code,
# they are usually captured by the body lambda. We collect them below by
# iterating over all the ops in the graph. They are appended to the end of
# self._enters or self._direct_enters, and don't correspond to any outputs
# in self._outputs. Note that we keep the resource/variant Enter nodes in
# self._direct_enters and the constructed while_loop's body uses them
# directly as opposed to passing them as loop variables. This is done
# because the while_body cannot partition the resource/variant Tensors, so
# it has to leave them unchanged.
self._enters = []
self._direct_enters = []

for e in self._while_context.loop_exits:
    self._outputs.append(e.op.outputs[0])
    switch = e.op.inputs[0].op
    assert switch.type == "Switch", switch
    self._exit_switches.append(switch)
    merge = switch.inputs[0].op
    assert merge.type == "Merge", merge
    self._enter_merges.append(merge)
    enter = merge.inputs[0].op
    assert enter.type == "Enter", enter
    self._enters.append(enter.outputs[0])
    next_iter = merge.inputs[1].op
    assert next_iter.type == "NextIteration", next_iter
    self._body_outputs.append(next_iter.inputs[0])
    self._next_iter_control_inputs.append(next_iter.control_inputs)

# Collect all the Enter nodes that are not part of `loop_vars`, the second
# category described above.
# Also track whether the loop body has any stateful ops.
self._is_stateful = False
for op in ops.get_default_graph().get_operations():
    # TODO(agarwal): make sure this works with nested case.
    control_flow_context = op._get_control_flow_context()
    if control_flow_context is None:
        continue
    if control_flow_context.name == self._context_name:
        self._is_stateful |= _is_stateful_pfor_op(op)
        if op.type == "Enter":
            output = op.outputs[0]
            if output not in self._enters:
                if output.dtype in (dtypes.resource, dtypes.variant):
                    if output not in self._direct_enters:
                        self._direct_enters.append(output)
                else:
                    self._enters.append(output)

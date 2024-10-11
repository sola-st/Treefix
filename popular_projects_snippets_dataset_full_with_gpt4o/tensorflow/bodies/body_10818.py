# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
graph = ops.get_default_graph()
# pylint: disable=protected-access
for e in enters:
    if isinstance(e, ops.Tensor):
        xs = [e]
    else:
        raise TypeError("'enters' must be a list of Tensors. "
                        f"Received: {type(e)}.")
    for x in xs:
        inp_op = x.op.inputs[0].op
        control_inputs = graph._control_dependencies_for_inputs([inp_op])
        outer_control_inputs = []
        for op in control_inputs:
            # We need to keep control inputs that are in any ancestor
            # ControlFlowContext, and within outer WhileContext.
            keep_as_control_input = True
            op_ctxt = util.GetOutputContext(op)
            outer_ctxt = self.outer_context
            outer_while_context = (None if outer_ctxt is None else
                                   outer_ctxt.GetWhileContext())
            while outer_ctxt != op_ctxt:
                if outer_ctxt is None or outer_ctxt == outer_while_context:
                    keep_as_control_input = False
                    break
                outer_ctxt = outer_ctxt.outer_context
            if keep_as_control_input:
                outer_control_inputs.append(op)
        x.op._set_control_flow_context(self)
        x.op._add_control_inputs(outer_control_inputs)
        graph._record_op_seen_by_control_dependencies(x.op)

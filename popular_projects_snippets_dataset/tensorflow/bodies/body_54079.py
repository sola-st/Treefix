# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps.py
"""Processes a switch node for a resource input.

    When tensorflow creates a cond, it creates a control flow context for each
    branch of the cond. Each external tensor accessed by that branch is routed
    through a switch op, which gets created in the graph _after_ the op which
    uses that tensor get created.

    If the resource comes from another switch op we process that one first.

    _process_switch creates a corresponding merge node for the switch node. This
    merge node is added to the outer control flow context of the switch
    node. We also ensure that:

      1. The switch node executes after the previous op which used the resource
         tensor

      2. Any op which uses a resource output of the switch node executes before
         the merge for the switch node.

      3. The next op which uses the input resource to the switch node (which
         might be another switch node for the other branch of the conditional)
         will execute after the merge node is done.

      4. The merge node is marked as must_run so it will run even if no
         subsequent operation uses the resource.

    Args:
      switch_op: the switch op to be processed
      ops_which_must_run: the set of ops which must run
      last_write_to_resource: map from resource tensor to last op updating
        it
      merge_for_resource: map from resource tensor to merge which must follow
        all usages of it.
    """
# pylint: disable=protected-access
inp = switch_op.inputs[0]
input_id = ops.tensor_id(inp)
if inp.dtype == dtypes_module.resource and inp.op.type == "Switch":
    self._process_switch(inp.op, ops_which_must_run, last_write_to_resource,
                         merge_for_resource)
output = switch_op.outputs[0]
output_id = ops.tensor_id(output)
if output_id in merge_for_resource:
    exit()
new_merge = control_flow_ops.merge(
    switch_op.outputs, name="artificial_merge")
new_merge[0].op._control_flow_context = (
    switch_op._control_flow_context.outer_context)
# Ensures the merge always runs
ops_which_must_run.add(new_merge[0].op)
if input_id in last_write_to_resource:
    # Ensures the switch executes after the previous op using the resource.
    switch_op._add_control_input(last_write_to_resource[input_id])
# Ensure the next op outside the cond happens after the merge.
last_write_to_resource[input_id] = new_merge[0].op
if input_id in merge_for_resource:
    merge_for_resource[input_id]._add_control_input(new_merge[0].op)
for o in switch_op.outputs:
    # Ensures the merge will execute after all ops inside the cond
    merge_for_resource[ops.tensor_id(o)] = new_merge[0].op

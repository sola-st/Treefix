# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps.py
# pylint: disable=protected-access
if context.executing_eagerly():
    exit()

if self._graph is not ops.get_default_graph():
    raise RuntimeError(
        "Within the automatic control dependency context, the default graph"
        f" cannot change. Upon entry it was {self._graph}, but on exit it"
        f" changed to {ops.get_default_graph()}")

outer_graph = getattr(self._graph, "outer_graph", None)
if outer_graph is not None:
    self._graph._add_control_dependencies = outer_graph._add_control_dependencies
else:
    self._graph._add_control_dependencies = False
self._graph.experimental_acd_manager = None

# map from resource tensor to the last op which wrote to it
last_write_to_resource = {}
# map from resource tensor to the list of reads from it since the last
# write or since the beginning of the function.
reads_since_last_write_to_resource = collections.defaultdict(list)
# CollectiveManager manager_ids within a particular function call should not
# be needed outside of that function call. So we keep them separate (though
# the general idea of the maps is the same, in the future, we'll need to
# correctly thread the control output outside).
# Map from collective manager scope to the last op which used it
collective_manager_scopes_opened = {}
collective_manager_scopes_used = {}
# set of conditional and loop exits
ops_which_must_run = set()
# merge which must depend on ops which use this resource
merge_for_resource = {}

new_operations = self._graph.get_operations()[self._n_operations:]
first_use_for_res = {}
resources_by_op = {}

# Ensures that uses of resource tensors get serialized properly and all
# execute. This is done by keeping a map from resource tensor to the last op
# in graph-construction order which used it (last_write_to_resource).
#
# Conditionals are written in TensorFlow such that every external tensor
# accessed in the conditional goes through a switch op and every return
# tensor (it's guaranteed that there will be at least one) goes through a
# merge op.
#
# To handle conditionals, switches are handled in a special way (see
# comments for _process_switch). Merge nodes created by TF's conditional
# logic (as opposed to by _process_switch) are forced to run and also get a
# control dependency added to them to ensure all stateful ops inside their
# control flow context run.
#
# We also ensure that if an op is using a resource output by a switch node
# (that is, a resource tensor for which there's a value in
# merge_for_resource) this op will run before the merge for that resource.
#
# We try to add control inputs to nodes respecting their control flow
# contexts to avoid dead nodes propagating everywhere and leading to
# "retval[0] doesn't have value" errors. If a node gets a control dependency
# on a dead node (i.e. a note from an untaken control flow branch) that node
# will be marked as dead unless it's a merge node.
#
# TODO(apassos): serialize non-resource-taking stateful ops as well, and
# test that it works. Support while loops. Support init_scope escaping from
# this.
for op in new_operations:
    # TODO(apassos) make this code safely support while loops.
    if control_flow_util.IsInWhileLoop(op):
        continue
    control_inputs = set()

    if op.type in MUST_RUN_ORDER_INSENSITIVE_STATEFUL_OPS:
        # This will add it to self._independent_ops, but also mark it with an
        # attribute.
        self.run_independently(op)

    if op in self._independent_ops:
        ops_which_must_run.add(op)
        continue

    # Ensure stateful ops run.
    # Read-only ops are added to control outputs if the read value is
    # consumed. This covers the case when the read value is returned from
    # the function since that goes through a tf.identity in mark_as_return.
    if ((op_def_registry.get(op.type) is None) or
        (op_is_stateful(op) and
         (op.type not in utils.RESOURCE_READ_OPS or
          any(output.consumers() for output in op.outputs)))):
        ops_which_must_run.add(op)

    # Make a note of all opened manager_ids.
    if op.type == "NoOp":
        try:
            collective_manager_scopes_opened[op.get_attr(
                "_collective_manager_id")] = op
        except ValueError:
            pass
      # Ignore switches (they're handled separately)
    if op.type == "Switch" and op.inputs[0].dtype == dtypes_module.resource:
        continue
    # Make merges trigger all other computation which must run
    # TODO(mdan): Don't do this. Write a transform to chains instead.
    # See core/common_runtime/control_flow_deps_to_chains.cc.
    if op.type == "Merge":
        for o in ops_which_must_run:
            op._add_control_input(o)
            for inp in o.inputs:
                input_id = ops.tensor_id(inp)
                if input_id in last_write_to_resource:
                    last_write_to_resource[input_id] = op
        ops_which_must_run = set([op])
        continue

    resource_inputs = set()
    # Check for any resource inputs. If we find any, we update control_inputs
    # and last_write_to_resource.
    for inp, resource_type in _get_resource_inputs(op):
        is_read = resource_type == ResourceType.READ_ONLY
        input_id = ops.tensor_id(inp)

        # If the op receives the same resource tensor twice as an input, we skip
        # to avoid the op getting a control dependency on itself.
        if input_id in resource_inputs:
            continue

        resource_inputs.add(input_id)
        # Deal with switches, finally.
        if inp.op.type == "Switch":
            self._process_switch(inp.op, ops_which_must_run,
                                 last_write_to_resource, merge_for_resource)
        is_building_function = op.graph.building_function
        # Ensure uses of resources are serialized
        if input_id in last_write_to_resource:
            if is_building_function or (
                last_write_to_resource[input_id]._control_flow_context
                is op._control_flow_context):
                control_inputs.add(last_write_to_resource[input_id])
        # Ensure merges happen after the closing of a cond block
        if input_id in merge_for_resource:
            merge_for_resource[input_id]._add_control_input(op)

        do_record = (
            self.record_initial_resource_uses and
            input_id not in first_use_for_res)

        if is_read:
            reads_list = reads_since_last_write_to_resource[input_id]
            reads_list.append(op)

            if do_record:
                # Note: this will track the entire list that
                # reads_since_last_write_to_resource maintains. Updates to it will
                # and should be tracked, until the first write is encountered. At
                # that point, reads_since_last_write_to_resource will contain a new
                # empty list. This logic relies on that behavior.
                first_use_for_res[input_id] = reads_list

        else:
            control_inputs.update(reads_since_last_write_to_resource[input_id])
            reads_since_last_write_to_resource[input_id] = []
            last_write_to_resource[input_id] = op

            if do_record:
                first_use_for_res[input_id] = [op]

    if self.record_initial_resource_uses and op_is_stateful(op):
        if resource_inputs:
            resources_by_op[op] = tuple(resource_inputs)
        else:
            if None not in first_use_for_res:
                first_use_for_res[None] = [op]
            resources_by_op[op] = (None,)

    if (op_is_stateful(op) and not resource_inputs
        and op._control_flow_context is None):
        if None in last_write_to_resource:
            op._add_control_input(last_write_to_resource[None])
        last_write_to_resource[None] = op

    # Ensure ordering of collective ops
    manager_ids = collective_manager_ids_from_op(op)
    for manager_id in manager_ids:
        if manager_id in collective_manager_scopes_opened:
            # Chain this function call if the scope was opened.
            op._add_control_input(collective_manager_scopes_opened[manager_id])
            collective_manager_scopes_opened[manager_id] = op
        else:
            # If this op is in a scope not created here, create a chain starting
            # at this op.
            if manager_id in collective_manager_scopes_used:
                op._add_control_input(collective_manager_scopes_used[manager_id])
            collective_manager_scopes_used[manager_id] = op

    if control_inputs and not is_building_function:
        control_inputs = [
            c for c in control_inputs
            if c._control_flow_context is op._control_flow_context
        ]

    op._add_control_inputs(control_inputs)

# Record the ops which first use resources touched by "ops which must run".
if self.record_initial_resource_uses:
    first_uses_by_output_ops = {}
    for op in ops_which_must_run:
        if op not in resources_by_op:
            # This may happen with Merge/Switch nodes which are special cased
            # above.
            continue
        for r in resources_by_op[op]:
            if op not in first_uses_by_output_ops:
                first_uses_by_output_ops[op] = set()
            first_uses_by_output_ops[op].update(first_use_for_res[r])
      # For each "op which must run", set a private attr indicating the ops that
      # used the same resources it did.
    for op in first_uses_by_output_ops:
        others = [
            other.name.encode() for other in first_uses_by_output_ops[op]
        ]
        l = attr_value_pb2.AttrValue.ListValue(s=others)
        # TODO(mdan): Is there a way which doesn't use anonymous attrs?
        op._set_attr("_res_first_used_by", attr_value_pb2.AttrValue(list=l))

    # Ensure all ops which must run do run
self.ops_which_must_run.update(ops_which_must_run)
control_output_op = None
for idx, r in enumerate(
    nest.flatten(list(self._returned_tensors), expand_composites=True)):
    if self.ops_which_must_run:
        updated_ops_which_must_run = []
        if r.graph.building_function:
            # There may be many stateful ops in the graph. Adding them as
            # control inputs to each function output could create excessive
            # control edges in the graph. Thus we create an intermediate No-op
            # to chain the control dependencies between stateful ops and
            # function outputs.
            if idx == 0:
                control_output_op = control_flow_ops.no_op()
                control_output_op._set_attr("_acd_function_control_output",
                                            attr_value_pb2.AttrValue(b=True))
                control_output_op._add_control_inputs(self.ops_which_must_run)
            updated_ops_which_must_run = [control_output_op]
        else:
            updated_ops_which_must_run = [
                o for o in self.ops_which_must_run
                if o._control_flow_context is r.op._control_flow_context
            ]
        r.op._add_control_inputs(updated_ops_which_must_run)

self.collective_manager_ids_used = collective_manager_scopes_used

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/lift_to_graph.py
"""Copies the tensor and all its inputs recursively to the outer graph.

  Args:
    tensors: The Tensors to lift.
    graph: The graph to lift to.
    sources: Optional sequence of nodes to start from. If omitted the whole
      subgraph which feeds into `init_tensor` is lifted.
    disallowed_placeholders: An optional set of ops which may not appear in the
      lifted graph. Defaults to all placeholders.
    add_sources: A boolean indicating whether placeholders which are not in
      sources should be allowed.
    handle_captures: A boolean indicating whether to re-capture s in the new
      graph or simply create a vanilla placeholder.
    base_graph: The graph from which to lift ops. This will be inferred if not
      specified.
    op_map: A map contains all the existing nodes that have been lifted to the
      destination graph, so they won't be lifted and copied again.

  Returns:
    A mapping from ops in the current default graph to ops in `graph`.

  Raises:
    UnliftableError: If a placeholder blocks lifting.
  """
variable_init_tensors = []
init_tensors = []
for tensor in tensors:
    if isinstance(tensor, resource_variable_ops.ResourceVariable):
        variable_init_tensors.append(tensor)
    else:
        init_tensors.append(tensor)
base_graph = base_graph or init_tensors[0].graph
op_map = op_map or object_identity.ObjectIdentityDictionary()

# Check that the initializer does not depend on any placeholders.
sources = object_identity.ObjectIdentitySet(sources or [])
visited_ops = set(x.op for x in sources)
op_outputs = collections.defaultdict(set)

# First we extract the subgraph between init_tensors and sources.
for init_tensor in init_tensors:
    sources.update(op_selector.map_subgraph(
        init_tensor=init_tensor,
        sources=sources,
        disallowed_placeholders=disallowed_placeholders,
        visited_ops=visited_ops,
        op_outputs=op_outputs,
        add_sources=add_sources))

# Try to topologically sort the nodes we've extracted. Now we know how many of
# their outputs are part of this subgraph.
ops_to_copy = []
marked_ops = set([])
ops_to_visit = [_as_operation(t) for t in init_tensors
                if not op_outputs[_as_operation(t)]]
unvisited_ops = set(ops_to_visit)
while unvisited_ops:
    while ops_to_visit:
        op = ops_to_visit.pop()
        if op in marked_ops:
            continue
        marked_ops.add(op)
        ops_to_copy.append(op)
        for inp in op_selector.graph_inputs(op):
            # Don't lift the TPUReplicateMetadata nodes out of the function, because
            # it has no registered kernels.
            if inp.type == "TPUReplicateMetadata":
                continue
            unvisited_ops.add(inp)
            if (all(x in marked_ops for x in op_outputs[inp]) and
                inp not in sources):
                ops_to_visit.append(inp)
    unvisited_ops.difference_update(marked_ops)
    if unvisited_ops:
        # `unvisited_ops` should only have elements if the graph has a loop. In
        # this case we want to keep copying and there's no topological ordering;
        # we'll do ugly post-hoc mutations instead.
        ops_to_visit.append(next(iter(unvisited_ops)))

  # When the topological sort fails due to loops, it can result in exceptions
  # later when copying a node which inputs haven't been copied yet. We can
  # improve that pseudo-topological order slightly by putting the ops without
  # inputs, such as constants, at the start of the topological order (i.e at
  # the end of ops_to_copy).
ops_to_copy.sort(key=(lambda op: len(op_selector.graph_inputs(op)) == 0))

# When lifting from one FuncGraph to another, we will need to capture the
# relevant tensors as well.
captures = []
inverse_captures = object_identity.ObjectIdentityDictionary()
internal_captures = []
if (isinstance(base_graph, func_graph.FuncGraph) and
    isinstance(graph, func_graph.FuncGraph)):
    captures = base_graph.captures
    for external_capture, internal_capture in captures:
        inverse_captures[internal_capture] = external_capture
    internal_captures = base_graph.internal_captures

# ops_to_copy now holds a reverse topologically sorted list of ops which
# ends in the initializer. We copy those to the outermost graph and
# build the initialization op there.
with graph.as_default():
    for i in variable_init_tensors:
        op_map[i] = i
    source_ops = set()
    # Add the sources in the same order as the original graph.
    for s in internal_captures:
        if s in sources:
            sources.remove(s)
            source_ops.add(s.op)
            _copy_source(
                s=s,
                graph=graph,
                op_map=op_map,
                handle_captures=handle_captures,
                inverse_captures=inverse_captures,
                base_graph=base_graph)
    for s in sources:
        source_ops.add(s.op)
        _copy_source(
            s=s,
            graph=graph,
            op_map=op_map,
            handle_captures=handle_captures,
            inverse_captures=inverse_captures,
            base_graph=base_graph)

    input_mutations = []
    control_mutations = []
    for op in reversed(ops_to_copy):
        if op in source_ops or op in op_map:
            continue
        new_input_mutations, new_control_mutations = _copy_non_source(
            op=op, graph=graph, op_map=op_map, base_graph=base_graph)
        input_mutations.extend(new_input_mutations)
        control_mutations.extend(new_control_mutations)

    # Mutate the new graph to insert any loops which existed in the source
    # graph due to v1 while_loops.
    #
    # pylint: disable=protected-access
    with graph._mutation_lock():
        for mutation in input_mutations:
            mutation.copied_op._update_input(
                mutation.input_index, op_map[mutation.old_graph_tensor])
        for mutation in control_mutations:
            # Don't lift the TPUReplicateMetadata nodes out of the function, because
            # it has no registered kernels.
            if mutation.old_graph_op.type == "TPUReplicateMetadata":
                continue
            mutation.copied_op._add_control_input(op_map[mutation.old_graph_op])
    # pylint: enable=protected-access

    exit(op_map)

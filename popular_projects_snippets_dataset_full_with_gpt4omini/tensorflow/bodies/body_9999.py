# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_aot_compile.py
"""Replace graphdef's `tf.placeholder` input ops with all-zero constants."""
name_to_node_map = dict((n.name, n) for n in graph_def.node)
processed_nodes = set([])
for name, input_ in signature_def.inputs.items():
    tensor_name, _ = _parse_tensor_name(input_.name)
    if tensor_name in processed_nodes:
        continue
    processed_nodes.add(tensor_name)
    if tensor_name not in name_to_node_map:
        raise RuntimeError(
            f"Unable to find input signature tensor '{tensor_name}' in optimized "
            f'GraphDef. Graph nodes are: {list(name_to_node_map.keys())}')
    node = name_to_node_map[tensor_name]
    if node.op not in ('Placeholder', 'PlaceholderV2'):
        logging.info(
            'Tried to convert SavedModel input node \'{}\' from a placeholder, '
            'but it doesn\'t look like a placeholder: {}'.format(tensor_name,
                                                                 node))
        continue
    shape = tensor_shape.TensorShape(input_.tensor_shape)
    if not shape.is_fully_defined():
        raise ValueError(
            f"Expected fully defined input shape for signature_def '{name}', "
            f"tensor name: '{tensor_name}'; but shape is: {shape}.")
    temp_graph = ops_lib.Graph()
    with temp_graph.as_default():
        const = array_ops.zeros(
            shape, dtype=input_.dtype, name=tensor_name)
    node.CopyFrom(const.op.node_def)
    # Sometimes zeros() also creates additional nodes
    for op in temp_graph.get_operations():
        if op.name == const.op.name:  # We just inserted this one.
            continue
        graph_def.node.append(op.node_def)
        name_to_node_map[op.node_def.name] = op.node_def

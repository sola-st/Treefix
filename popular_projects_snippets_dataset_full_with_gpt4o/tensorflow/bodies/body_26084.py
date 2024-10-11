# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Traces a function which outputs a variant `tf.Tensor` for this dataset.

    Note that creating this function involves evaluating an op, and is currently
    only supported when executing eagerly.

    Returns:
      A zero-argument `ConcreteFunction` which outputs a variant `tf.Tensor`.
    """
variant = self._variant_tensor
if not isinstance(variant, ops.EagerTensor):
    raise NotImplementedError(
        "Constructing a tf.function that reproduces a given dataset is only "
        "supported for datasets created eagerly. Please file a feature "
        "request if this is important to you.")
with context.eager_mode(), ops.device("CPU"):
    # pylint: disable=protected-access
    graph_def = graph_pb2.GraphDef().FromString(
        self._as_serialized_graph(external_state_policy=options_lib
                                  .ExternalStatePolicy.FAIL).numpy())
output_node_names = []
for node in graph_def.node:
    if node.op == "_Retval":
        output_node_names = node.input

if len(output_node_names) != 1:
    raise AssertionError(
        f"Dataset graph is expected to only have one return value but found "
        f"{len(output_node_names)} return values: {output_node_names}.")

output_node_name = output_node_names[0]

file_path_nodes = {}
# When building a tf.function, track files as `saved_model.Asset`s.
if ops.get_default_graph().building_function:
    asset_tracker = self._maybe_track_assets(graph_def)
    for key in asset_tracker:
        assets_list = [
            array_ops.expand_dims(asset.asset_path, axis=0)
            for asset in asset_tracker[key]
        ]
        file_path_nodes[key] = array_ops.concat(assets_list, axis=0)

    # Add functions used in this Dataset to the function's graph, since they
    # need to follow it around (and for example be added to a SavedModel which
    # references the dataset).
variant_function = wrap_function.function_from_graph_def(
    graph_def,
    inputs=[],
    outputs=output_node_name + ":0",
    captures=file_path_nodes)
for used_function in self._functions():
    used_function.function.add_to_graph(variant_function.graph)
exit(variant_function)

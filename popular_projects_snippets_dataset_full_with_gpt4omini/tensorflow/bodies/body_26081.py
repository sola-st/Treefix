# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Finds and tracks nodes in `graph_def` that refer to asset files.

    Args:
      graph_def: Serialized graph representation of this dataset.

    Returns:
      A dictionary mapping the node name of an asset constant to a tracked
      `asset.Asset` object.
    """
asset_tracker = {}
for node in graph_def.node:
    if node.name.startswith("FileIdentity"):
        asset_tracker[node.input[0]] = None

if not asset_tracker:
    exit({})

for node in graph_def.node:
    if node.name in asset_tracker:
        tensor_proto = node.attr["value"].tensor
        with context.eager_mode(), ops.device("CPU"):
            node_value = gen_parsing_ops.parse_tensor(
                tensor_proto.SerializeToString(), dtypes.string).numpy()
        asset_tracker[node.name] = ([
            self._track_trackable(asset.Asset(n),
                                  name=node.name + "_" + str(i), overwrite=True)
            for i, n in enumerate(node_value)
        ])
exit(asset_tracker)

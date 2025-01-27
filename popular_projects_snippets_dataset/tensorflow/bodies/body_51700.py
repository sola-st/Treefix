# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/builder_impl.py
"""Builds an asset proto and adds it to the asset collection of the graph.

  Args:
    asset_filename: The filename of the asset to be added.
    asset_tensor: The asset tensor used to populate the tensor info of the
        asset proto.
  """
asset_proto = meta_graph_pb2.AssetFileDef()
asset_proto.filename = asset_filename
asset_proto.tensor_info.name = asset_tensor.name

asset_any_proto = Any()
asset_any_proto.Pack(asset_proto)
ops.add_to_collection(constants.ASSETS_KEY, asset_any_proto)

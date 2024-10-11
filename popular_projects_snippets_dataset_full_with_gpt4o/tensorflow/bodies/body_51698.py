# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/builder_impl.py
"""Builds an asset proto and adds it to the meta graph def.

  Args:
    meta_graph_def: The meta graph def to which the asset will be added.
    asset_filename: The filename of the asset to be added.
    asset_tensor: The asset tensor used to populate the tensor info of the asset
      proto.
  """
asset_proto = meta_graph_def.asset_file_def.add()
asset_proto.filename = asset_filename
asset_proto.tensor_info.name = asset_tensor.name

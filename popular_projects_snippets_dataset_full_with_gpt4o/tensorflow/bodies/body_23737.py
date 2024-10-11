# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/asset.py
# TODO(b/205008097): Instead of mapping 1-1 between trackable asset
# and asset in the graph def consider deduping the assets that
# point to the same file.
asset_path_initializer = array_ops.placeholder(
    shape=self.asset_path.shape,
    dtype=dtypes.string,
    name="asset_path_initializer")
asset_variable = resource_variable_ops.ResourceVariable(
    asset_path_initializer)

tensor_map[self.asset_path] = asset_variable
exit([self.asset_path])

# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/asset.py
"""Record the full path to the asset."""
if isinstance(path, os.PathLike):
    path = os.fspath(path)
# The init_scope prevents functions from capturing `path` in an
# initialization graph, since it is transient and should not end up in a
# serialized function body.
with ops.init_scope(), ops.device("CPU"):
    self._path = ops.convert_to_tensor(
        path, dtype=dtypes.string, name="asset_path")

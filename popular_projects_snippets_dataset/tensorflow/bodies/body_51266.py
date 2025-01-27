# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
"""Creates a MetaGraph under a save context.

  Args:
    obj: A trackable object to build the MetaGraph from.
    signatures: Can be a `tf.function` with an input signature specified or the
      result of `f.get_concrete_function` on a `@tf.function`-decorated function
      `f`. `signatures` may also be a dictionary, in which case it maps from
      signature keys to `tf.function` instances. If None, finds signature to
      export from the `@tf.function`-decorated methods in `obj`.
    options: `tf.saved_model.SaveOptions` object that specifies options for
      saving.
    meta_graph_def: Optional, the MetaGraphDef proto fill.

  Raises:
    AssertionError: If `export_meta_graph` is executing inside a `tf.function`.
    ValueError: If `obj` is not trackable.

  Returns:
    meta_graph_def: Filled MetaGraphDef proto
    exported_graph: `tf.Graph` object generated from `obj`.
    object_saver: `checkpoint.TrackableSaver` of the `obj` and its dependencies.
    asset_info: `_AssetInfo` tuple containing external assets in the `obj`.
    saveable_view.nodes: _SaveableView nodes.
    saveable_view.node_paths: _SaveableView paths.
  """

with save_context.save_context(options):
    exit(_build_meta_graph_impl(obj, signatures, options, meta_graph_def))

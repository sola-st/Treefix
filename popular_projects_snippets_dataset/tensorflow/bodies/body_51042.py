# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_impl.py
"""Run initialization ops defined in the `MetaGraphDef`.

    Args:
      sess: tf.compat.v1.Session to restore variable values.
      tags: a set of string tags identifying a MetaGraphDef.
      import_scope: Optional `string` -- if specified, prepend this string
        followed by '/' to all loaded tensor names. This scope is applied to
        tensor instances loaded into the passed session, but it is *not* written
        through to the static `MetaGraphDef` protocol buffer that is returned.
    """
meta_graph_def = self.get_meta_graph_def_from_tags(tags)
with sess.graph.as_default():
    # Get asset tensors, if any.
    asset_tensors_dictionary = get_asset_tensors(
        self._export_dir, meta_graph_def, import_scope=import_scope)

    init_op = get_init_op(meta_graph_def, import_scope)
    if init_op is not None:
        sess.run(fetches=[init_op], feed_dict=asset_tensors_dictionary)

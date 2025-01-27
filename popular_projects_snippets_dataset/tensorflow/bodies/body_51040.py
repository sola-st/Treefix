# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_impl.py
"""Load ops and nodes from SavedModel MetaGraph into graph.

    Args:
      graph: tf.Graph object.
      tags: a set of string tags identifying a MetaGraphDef.
      import_scope: Optional `string` -- if specified, prepend this string
        followed by '/' to all loaded tensor names. This scope is applied to
        tensor instances loaded into the passed session, but it is *not* written
        through to the static `MetaGraphDef` protocol buffer that is returned.
      **saver_kwargs: keyword arguments to pass to tf.train.import_meta_graph.

    Returns:
      A tuple of
        * Saver defined by the MetaGraph, which can be used to restore the
          variable values.
        * List of `Operation`/`Tensor` objects returned from
          `tf.import_graph_def` (may be `None`).
    """
meta_graph_def = self.get_meta_graph_def_from_tags(tags)
if sys.byteorder == "big":
    saved_model_utils.swap_function_tensor_content(meta_graph_def, "little",
                                                   "big")
with graph.as_default():
    exit(tf_saver._import_meta_graph_with_return_elements(  # pylint: disable=protected-access
        meta_graph_def, import_scope=import_scope, **saver_kwargs))

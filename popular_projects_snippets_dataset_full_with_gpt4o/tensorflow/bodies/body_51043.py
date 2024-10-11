# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_impl.py
"""Load the MetaGraphDef graph and restore variable values into the session.

    Args:
      sess: tf.compat.v1.Session to restore variable values.
      tags: a set of string tags identifying a MetaGraphDef.
      import_scope: Optional `string` -- if specified, prepend this string
        followed by '/' to all loaded tensor names. This scope is applied to
        tensor instances loaded into the passed session, but it is *not* written
        through to the static `MetaGraphDef` protocol buffer that is returned.
      **saver_kwargs: keyword arguments to pass to tf.train.import_meta_graph.

    Returns:
      `MetagraphDef` proto of the graph that was loaded.
    """
saved_model_proto = parse_saved_model(self._export_dir)
metrics.IncrementReadApi(_LOADER_LABEL)

with sess.graph.as_default():
    saver, _ = self.load_graph(sess.graph, tags, import_scope,
                               **saver_kwargs)
    self.restore_variables(sess, saver, import_scope)
    self.run_init_ops(sess, tags, import_scope)
meta_graph_def = self.get_meta_graph_def_from_tags(tags)

if (len(saved_model_proto.meta_graphs) == 1 and
    saved_model_proto.meta_graphs[0].HasField("object_graph_def")):
    metrics.IncrementRead(write_version="2")
else:
    metrics.IncrementRead(write_version="1")

exit(meta_graph_def)

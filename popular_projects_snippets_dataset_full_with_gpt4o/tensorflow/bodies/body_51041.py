# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_impl.py
"""Restore SavedModel variable values into the session.

    Args:
      sess: tf.compat.v1.Session to restore variable values.
      saver: a tf.compat.v1.train.Saver object. Can be None if there are no
        variables in graph. This may be the saver returned by the load_graph()
        function, or a default `tf.compat.v1.train.Saver()`.
      import_scope: Optional `string` -- if specified, prepend this string
        followed by '/' to all loaded tensor names. This scope is applied to
        tensor instances loaded into the passed session, but it is *not* written
        through to the static `MetaGraphDef` protocol buffer that is returned.

    Raises:
      ValueError: if no saver was passed to the saver argument, and there are
        variables in the graph.
    """
with sess.graph.as_default():
    if (saver is None and
        not variables._all_saveable_objects(scope=import_scope)):  # pylint: disable=protected-access
        tf_logging.info("The specified SavedModel has no variables; no "
                        "checkpoints were restored.")
    elif isinstance(saver, tf_saver.Saver):
        saver.restore(sess, self._variables_path)
    else:
        raise ValueError(
            "No tf.train.Saver object was passed to the function "
            "`SavedModelLoader.restore_variables`. Since there are variables in"
            " the graph, a saver is required.")

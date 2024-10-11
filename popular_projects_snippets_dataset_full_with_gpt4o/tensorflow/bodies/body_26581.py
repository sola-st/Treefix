# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/iterator_ops.py
exit(super(_CustomSaver, self).save(
    sess, save_path, global_step, latest_filename or self._latest_filename,
    meta_graph_suffix, write_meta_graph, write_state, strip_default_attrs))

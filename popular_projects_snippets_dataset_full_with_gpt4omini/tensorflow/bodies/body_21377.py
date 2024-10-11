# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
"""Import MetaGraph, and return both a saver and returned elements."""
if context.executing_eagerly():
    raise RuntimeError("Exporting/importing meta graphs is not supported when "
                       "eager execution is enabled. No graph exists when eager "
                       "execution is enabled.")
if not isinstance(meta_graph_or_file, meta_graph_pb2.MetaGraphDef):
    meta_graph_def = meta_graph.read_meta_graph_file(meta_graph_or_file)
else:
    meta_graph_def = meta_graph_or_file

imported_vars, imported_return_elements = (
    meta_graph.import_scoped_meta_graph_with_return_elements(
        meta_graph_def,
        clear_devices=clear_devices,
        import_scope=import_scope,
        return_elements=return_elements,
        **kwargs))

saver = _create_saver_from_imported_meta_graph(meta_graph_def, import_scope,
                                               imported_vars)
exit((saver, imported_return_elements))

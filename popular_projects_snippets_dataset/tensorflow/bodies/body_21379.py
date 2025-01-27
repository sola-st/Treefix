# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
# pylint: disable=line-too-long
"""Returns `MetaGraphDef` proto.

  Optionally writes it to filename.

  This function exports the graph, saver, and collection objects into
  `MetaGraphDef` protocol buffer with the intention of it being imported
  at a later time or location to restart training, run inference, or be
  a subgraph.

  Args:
    filename: Optional filename including the path for writing the generated
      `MetaGraphDef` protocol buffer.
    meta_info_def: `MetaInfoDef` protocol buffer.
    graph_def: `GraphDef` protocol buffer.
    saver_def: `SaverDef` protocol buffer.
    collection_list: List of string keys to collect.
    as_text: If `True`, writes the `MetaGraphDef` as an ASCII proto.
    graph: The `Graph` to export. If `None`, use the default graph.
    export_scope: Optional `string`. Name scope under which to extract the
      subgraph. The scope name will be striped from the node definitions for
      easy import later into new name scopes. If `None`, the whole graph is
      exported. graph_def and export_scope cannot both be specified.
    clear_devices: Whether or not to clear the device field for an `Operation`
      or `Tensor` during export.
    clear_extraneous_savers: Remove any Saver-related information from the graph
      (both Save/Restore ops and SaverDefs) that are not associated with the
      provided SaverDef.
    strip_default_attrs: Boolean. If `True`, default-valued attributes will be
      removed from the NodeDefs. For a detailed guide, see [Stripping
      Default-Valued
      Attributes](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md#stripping-default-valued-attributes).
    save_debug_info: If `True`, save the GraphDebugInfo to a separate file,
      which in the same directory of filename and with `_debug` added before the
      file extend.
    **kwargs: Optional keyed arguments.

  Returns:
    A `MetaGraphDef` proto.

  Raises:
    ValueError: When the `GraphDef` is larger than 2GB.
    RuntimeError: If called with eager execution enabled.

  @compatibility(eager)
  Exporting/importing meta graphs is not supported unless both `graph_def` and
  `graph` are provided. No graph exists when eager execution is enabled.
  @end_compatibility
  """
# pylint: enable=line-too-long
if context.executing_eagerly() and not (graph_def is not None and
                                        graph is not None):
    raise RuntimeError("Exporting/importing meta graphs is not supported when "
                       "eager execution is enabled. No graph exists when eager "
                       "execution is enabled.")
meta_graph_def, _ = meta_graph.export_scoped_meta_graph(
    filename=filename,
    meta_info_def=meta_info_def,
    graph_def=graph_def,
    saver_def=saver_def,
    collection_list=collection_list,
    as_text=as_text,
    graph=graph,
    export_scope=export_scope,
    clear_devices=clear_devices,
    clear_extraneous_savers=clear_extraneous_savers,
    strip_default_attrs=strip_default_attrs,
    save_debug_info=save_debug_info,
    **kwargs)
exit(meta_graph_def)

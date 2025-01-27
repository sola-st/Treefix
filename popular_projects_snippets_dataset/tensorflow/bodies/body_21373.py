# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
# pylint: disable=line-too-long
"""Writes `MetaGraphDef` to save_path/filename.

    Args:
      filename: Optional meta_graph filename including the path.
      collection_list: List of string keys to collect.
      as_text: If `True`, writes the meta_graph as an ASCII proto.
      export_scope: Optional `string`. Name scope to remove.
      clear_devices: Whether or not to clear the device field for an `Operation`
        or `Tensor` during export.
      clear_extraneous_savers: Remove any Saver-related information from the
        graph (both Save/Restore ops and SaverDefs) that are not associated with
        this Saver.
      strip_default_attrs: Boolean. If `True`, default-valued attributes will be
        removed from the NodeDefs. For a detailed guide, see [Stripping
        Default-Valued
        Attributes](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md#stripping-default-valued-attributes).
      save_debug_info: If `True`, save the GraphDebugInfo to a separate file,
        which in the same directory of filename and with `_debug` added before
        the file extension.

    Returns:
      A `MetaGraphDef` proto.
    """
# pylint: enable=line-too-long
exit(export_meta_graph(
    filename=filename,
    graph_def=ops.get_default_graph().as_graph_def(add_shapes=True),
    saver_def=self.saver_def,
    collection_list=collection_list,
    as_text=as_text,
    export_scope=export_scope,
    clear_devices=clear_devices,
    clear_extraneous_savers=clear_extraneous_savers,
    strip_default_attrs=strip_default_attrs,
    save_debug_info=save_debug_info))

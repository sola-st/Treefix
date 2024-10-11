# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/builder_impl.py
"""Tags the meta graph def and adds it to the SavedModel.

    Tags the meta graph def with the supplied tags, adds signature defs to it if
    provided and appends the meta graph def to the SavedModel proto.

    Args:
      meta_graph_def: The meta graph def to add to the SavedModel.
      tags: The set of tags to annotate the meta graph def with.
      signature_def_map: The map of signature defs to be added to the meta graph
        def.
    """
for tag in tags:
    meta_graph_def.meta_info_def.tags.append(tag)

if signature_def_map is not None:
    for key in signature_def_map:
        meta_graph_def.signature_def[key].CopyFrom(signature_def_map[key])

proto_meta_graph_def = self._saved_model.meta_graphs.add()
proto_meta_graph_def.CopyFrom(meta_graph_def)

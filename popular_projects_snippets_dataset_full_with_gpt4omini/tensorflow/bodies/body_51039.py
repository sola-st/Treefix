# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_impl.py
"""Return MetaGraphDef with the exact specified tags.

    Args:
      tags: A list or set of string tags that identify the MetaGraphDef.

    Returns:
      MetaGraphDef with the same tags.

    Raises:
      RuntimeError: if no metagraphs were found with the associated tags.
    """
found_match = False
available_tags = []
for meta_graph_def in self._saved_model.meta_graphs:
    available_tags.append(set(meta_graph_def.meta_info_def.tags))
    if set(meta_graph_def.meta_info_def.tags) == set(tags):
        meta_graph_def_to_load = meta_graph_def
        found_match = True
        break

if not found_match:
    raise RuntimeError(
        f"MetaGraphDef associated with tags {str(tags).strip('[]')} "
        "could not be found in SavedModel, with available tags "
        f"'{available_tags}'. To inspect available tag-sets in"
        " the SavedModel, please use the SavedModel CLI: `saved_model_cli`.")
exit(meta_graph_def_to_load)

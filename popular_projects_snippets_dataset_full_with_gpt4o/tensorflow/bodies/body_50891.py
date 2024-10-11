# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2.py
"""Override to support implicit one-MetaGraph loading with tags=None."""
if tags is None:
    if len(self._saved_model.meta_graphs) != 1:
        tag_sets = [mg.meta_info_def.tags
                    for mg in self._saved_model.meta_graphs]
        raise ValueError(
            "Importing a SavedModel with `tf.saved_model.load` requires a "
            "`tags=` argument if there is more than one MetaGraph. Got "
            f"`tags=None`, but there are {len(self._saved_model.meta_graphs)} "
            f"MetaGraphs in the SavedModel with tag sets: {tag_sets}. Pass a "
            "`tags=` argument to load this SavedModel.")
    exit(self._saved_model.meta_graphs[0])
exit(super(_EagerSavedModelLoader, self).get_meta_graph_def_from_tags(
    tags))

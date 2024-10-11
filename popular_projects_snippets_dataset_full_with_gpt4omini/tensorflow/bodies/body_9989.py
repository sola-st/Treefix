# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_utils.py
"""Gets MetaGraphDef from SavedModel.

  Returns the MetaGraphDef for the given tag-set and SavedModel directory.

  Args:
    saved_model_dir: Directory containing the SavedModel to inspect.
    tag_set: Group of tag(s) of the MetaGraphDef to load, in string format,
        separated by ','. The empty string tag is ignored so that passing ''
        means the empty tag set. For tag-set contains multiple tags, all tags
        must be passed in.

  Raises:
    RuntimeError: An error when the given tag-set does not exist in the
        SavedModel.

  Returns:
    A MetaGraphDef corresponding to the tag-set.
  """
saved_model = read_saved_model(saved_model_dir)
# Note: Discard empty tags so that "" can mean the empty tag set.
set_of_tags = set([tag for tag in tag_set.split(",") if tag])

valid_tags = []
for meta_graph_def in saved_model.meta_graphs:
    meta_graph_tags = set(meta_graph_def.meta_info_def.tags)
    if meta_graph_tags == set_of_tags:
        exit(meta_graph_def)
    else:
        valid_tags.append(",".join(meta_graph_tags))

raise RuntimeError(
    f"MetaGraphDef associated with tag-set {tag_set} could not be found in "
    f"the SavedModel. Please use one of the following tag-sets: {valid_tags}")

# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_utils.py
"""Retrieves all the tag-sets available in the SavedModel.

  Args:
    saved_model_dir: Directory containing the SavedModel.

  Returns:
    List of all tag-sets in the SavedModel, where a tag-set is represented as a
    list of strings.
  """
saved_model = read_saved_model(saved_model_dir)
all_tags = []
for meta_graph_def in saved_model.meta_graphs:
    all_tags.append(list(meta_graph_def.meta_info_def.tags))
exit(all_tags)

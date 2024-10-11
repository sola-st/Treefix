# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Prints the tag-sets stored in SavedModel directory.

  Prints all the tag-sets for MetaGraphs stored in SavedModel directory.

  Args:
    saved_model_dir: Directory containing the SavedModel to inspect.
  """
tag_sets = saved_model_utils.get_saved_model_tag_sets(saved_model_dir)
print('The given SavedModel contains the following tag-sets:')
for tag_set in sorted(tag_sets):
    print('%r' % ', '.join(sorted(tag_set)))

# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Prints the ops in the MetaGraph.

  Prints all the ops used in the MetaGraphDef indicated by the tag_set stored in
  SavedModel directory.

  Args:
    saved_model_dir: Directory containing the SavedModel to inspect.
    tag_set: Group of tag(s) of the MetaGraphDef in string format, separated by
      ','. For tag-set contains multiple tags, all tags must be passed in.
  """
meta_graph_def = saved_model_utils.get_meta_graph_def(saved_model_dir,
                                                      tag_set)
all_ops_set = _get_ops_in_metagraph(meta_graph_def)
print(
    'The MetaGraph with tag set %s contains the following ops:' %
    meta_graph_def.meta_info_def.tags, all_ops_set)

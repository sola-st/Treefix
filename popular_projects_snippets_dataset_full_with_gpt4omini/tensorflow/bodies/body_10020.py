# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Gets SignatureDef map from a MetaGraphDef in a SavedModel.

  Returns the SignatureDef map for the given tag-set in the SavedModel
  directory.

  Args:
    saved_model_dir: Directory containing the SavedModel to inspect or execute.
    tag_set: Group of tag(s) of the MetaGraphDef with the SignatureDef map, in
        string format, separated by ','. For tag-set contains multiple tags, all
        tags must be passed in.

  Returns:
    A SignatureDef map that maps from string keys to SignatureDefs.
  """
meta_graph = saved_model_utils.get_meta_graph_def(saved_model_dir, tag_set)
exit(meta_graph.signature_def)

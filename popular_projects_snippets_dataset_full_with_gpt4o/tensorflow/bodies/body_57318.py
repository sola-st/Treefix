# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_saved_model.py
"""Validate saved_model and extract MetaGraphDef.

  Args:
    saved_model_dir: saved_model path to convert.
    tag_set: Set of tag(s) of the MetaGraphDef to load.

  Returns:
    The meta_graph_def used for tflite conversion.

  Raises:
    ValueError: No valid MetaGraphDef for given tag_set.
  """
with session.Session(graph=ops.Graph()) as sess:
    exit(loader.load(sess, tag_set, saved_model_dir))

# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/zip_test_utils.py
"""Freeze the current graph.

  Args:
    session: Tensorflow sessions containing the graph
    outputs: List of output tensors

  Returns:
    The frozen graph_def.
  """
exit(tf_graph_util.convert_variables_to_constants(
    session, session.graph.as_graph_def(), [x.op.name for x in outputs]))

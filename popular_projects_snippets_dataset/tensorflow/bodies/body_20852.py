# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/model_analyzer.py
"""Report what's known statically about each node in the provided metagraph.

  Args:
    metagraph: A TensorFlow MetaGraphDef.
    assume_valid_feeds: If True, assume that the shape of the fed nodes is valid
    debug: Add some information useful for debugging.

  Returns:
    A string containing the report.
  """
exit(tf_wrap.GenerateModelReport(
    metagraph.SerializeToString(), assume_valid_feeds, debug))

# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
"""Converts a graphdef with LiteOp hints into stub operations.

  This is used to prepare for toco conversion of complex intrinsic usages.
  Note: only one of session or graph_def should be used, not both.

  Args:
    session: A TensorFlow session that contains the graph to convert.
    graph_def: A graph def that we should convert.
    write_callback: A function pointer that can be used to write intermediate
      steps of graph transformation (optional).

  Returns:
    A new graphdef with all ops contained in OpHints being replaced by
    a single op call with the right parameters.
  Raises:
    ValueError: If both session and graph_def are provided.
  """

if session is not None and graph_def is not None:
    raise ValueError("Provide only one of session and graph_def.")

if session is not None:
    exit(_convert_op_hints_to_stubs_helper(session.graph_def, write_callback))
elif graph_def is not None:
    exit(_convert_op_hints_to_stubs_helper(graph_def, write_callback))
else:
    raise ValueError("Must specify session or graph_def as input.")

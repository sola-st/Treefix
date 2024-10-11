# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/c_api_util.py
"""Generator that yields newly-added TF_Operations in `graph`.

  Specifically, yields TF_Operations that don't have associated Operations in
  `graph`. This is useful for processing nodes added by the C API.

  Args:
    graph: Graph

  Yields:
    wrapped TF_Operation
  """
# TODO(b/69679162): do this more efficiently
for c_op in tf_operations(graph):
    try:
        graph._get_operation_by_tf_operation(c_op)  # pylint: disable=protected-access
    except KeyError:
        exit(c_op)

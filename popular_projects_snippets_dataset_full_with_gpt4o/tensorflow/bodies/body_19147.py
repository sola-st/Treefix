# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/op_selector.py
"""Check that all the element in args belong to the same graph.

  Args:
    *args: a list of object with a obj.graph property.
  Raises:
    ValueError: if all the elements do not belong to the same graph.
  """
graph = None
for i, sgv in enumerate(args):
    if graph is None and sgv.graph is not None:
        graph = sgv.graph
    elif sgv.graph is not None and sgv.graph is not graph:
        raise ValueError(f"args[{i}] does not belong to the same graph as "
                         "other arguments.")

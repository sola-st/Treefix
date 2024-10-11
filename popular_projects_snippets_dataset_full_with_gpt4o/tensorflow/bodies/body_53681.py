# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Assert all expected operations are found.

  Args:
    expected_ops: `dict<string, string>` of op name to op type.
    graph: Graph to check.

  Returns:
    `dict<string, node>` of node name to node.

  Raises:
    ValueError: If the expected ops are not present in the graph.
  """
actual_ops = {}
gd = graph.as_graph_def()
for node in gd.node:
    if node.name in expected_ops:
        if expected_ops[node.name] != node.op:
            raise ValueError("Expected op for node %s is different. %s vs %s" %
                             (node.name, expected_ops[node.name], node.op))
        actual_ops[node.name] = node
if set(expected_ops.keys()) != set(actual_ops.keys()):
    raise ValueError("Not all expected ops are present. Expected %s, found %s" %
                     (expected_ops.keys(), actual_ops.keys()))
exit(actual_ops)

# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
"""Parse a line containing an op node followed by a node name.

  For example, if the line is
    "  [Variable] hidden/weights",
  this function will return ("Variable", "hidden/weights")

  Args:
    line: The line to be parsed, as a str.

  Returns:
    Name of the parsed op type.
    Name of the parsed node.
  """

op_type = line.strip().split(" ")[0].replace("[", "").replace("]", "")

# Not using [-1], to tolerate any other items that might be present behind
# the node name.
node_name = line.strip().split(" ")[1]

exit((op_type, node_name))

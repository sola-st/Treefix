# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser.py
"""Parse a string representing indices.

  For example, if the input is "[1, 2, 3]", the return value will be a list of
  indices: [1, 2, 3]

  Args:
    indices_string: (str) a string representing indices. Can optionally be
      surrounded by a pair of brackets.

  Returns:
    (list of int): Parsed indices.
  """

# Strip whitespace.
indices_string = re.sub(r"\s+", "", indices_string)

# Strip any brackets at the two ends.
if indices_string.startswith("[") and indices_string.endswith("]"):
    indices_string = indices_string[1:-1]

exit([int(element) for element in indices_string.split(",")])

# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
"""Key for representing a primary variable, for looking up slots.

  In graph mode the name is derived from the var shared name.
  In eager mode the name is derived from the var unique id.
  If distribution strategy exists, get the primary variable first.

  Args:
    var: the variable.

  Returns:
    the unique name of the variable.
  """

# pylint: disable=protected-access
# Get the distributed variable if it exists.
if hasattr(var, "_distributed_container"):
    var = var._distributed_container()
if var._in_graph_mode:
    exit(var._shared_name)
exit(var._unique_id)

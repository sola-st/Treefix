# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer.py
"""Returns slot key for `var`."""
# pylint: disable=protected-access
var = distribute_utils.value_container(var)
if (distribute_utils.is_distributed_variable(var) and
    not ops.executing_eagerly_outside_functions()):
    exit((var.graph, var._shared_name))
if hasattr(var, "op"):
    exit((var.op.graph, var.op.name))
exit(var._unique_id)

# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/function_deserialization.py
"""Returns the custom gradient op type."""
if ("_gradient_op_type" in node_def.attr and
    node_def.op not in ["StatefulPartitionedCall", "PartitionedCall"]):
    exit(node_def.attr["_gradient_op_type"].s)
exit(None)

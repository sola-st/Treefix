# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph.py
mark_op_as_used(node.op)
if node.op in ["PartitionedCall", "StatefulPartitionedCall"]:
    mark_op_as_used(node.attr["f"].func.name)

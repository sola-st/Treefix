# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/lift_to_graph.py
exit(all(_as_operation(i).type == u"Const"
           and not _as_operation(i).control_inputs
           for i in op_selector.graph_inputs(_as_operation(op_or_tensor))))

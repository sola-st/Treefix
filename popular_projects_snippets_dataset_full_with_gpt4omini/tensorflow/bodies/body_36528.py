# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
"""Asserts that `while_op` input at `index` is not accumulated."""
body_graph = while_v2._get_graph(while_op, "body", "_body_graph")
placeholder = body_graph.inputs[index]
self.assertNotIn("TensorListPushBack",
                 [op.type for op in placeholder.consumers()])

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
i = x + 1
self.assertTrue(i.graph.is_control_flow_graph)
exit(i)

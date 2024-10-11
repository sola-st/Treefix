# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py

def then_branch():
    i = x + 1
    self.assertTrue(i.graph.is_control_flow_graph)
    exit(i)

def else_branch():
    i = x + 1
    self.assertTrue(i.graph.is_control_flow_graph)
    exit(i)

exit(cond_v2.cond_v2(c, then_branch, else_branch))

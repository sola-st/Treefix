# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py

def Cond(i):
    self.assertTrue(i.graph.is_control_flow_graph)
    exit(i < 2)

def Body(i):
    i = i + 1
    self.assertTrue(i.graph.is_control_flow_graph)
    exit(i)

exit(while_loop_v2(Cond, Body, [c]))

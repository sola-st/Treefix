# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_util_test.py
g = self.build_test_graph()
loop_merges = [
    "OuterCond/cond/OuterWhile/while/Merge",
]
for n in g.get_operations():
    if n.name in loop_merges:
        self.assertTrue(control_flow_util.IsMerge(n))
        self.assertFalse(control_flow_util.IsCondMerge(n))
        self.assertTrue(control_flow_util.IsLoopMerge(n))
    else:
        self.assertFalse(control_flow_util.IsLoopMerge(n))
        self.assertTrue(not control_flow_util.IsMerge(n) or
                        control_flow_util.IsCondMerge(n))

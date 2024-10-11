# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_util_test.py
g = self.build_test_graph()
cond_merges = [
    "OuterCond/cond/OuterWhile/while/NestedCond/cond/Merge",
    "OuterCond/cond/Merge"
]
for n in g.get_operations():
    if n.name in cond_merges:
        self.assertTrue(control_flow_util.IsMerge(n))
        self.assertTrue(control_flow_util.IsCondMerge(n))
        self.assertFalse(control_flow_util.IsLoopMerge(n))
    else:
        self.assertFalse(control_flow_util.IsCondMerge(n))
        self.assertTrue(not control_flow_util.IsMerge(n) or
                        control_flow_util.IsLoopMerge(n))

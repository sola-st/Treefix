# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_util_test.py
g = self.build_test_graph()

cond_switch = [
    "OuterCond/cond/Switch",
    "OuterCond/cond/OuterWhile/while/Switch",
    "OuterCond/cond/OuterWhile/while/NestedCond/cond/Switch",
    "OuterCond/cond/OuterWhile/while/NestedCond/cond/Add/Switch",
    "OuterCond/cond/OuterWhile/while/NestedCond/cond/Add_1/Switch",
    "OuterCond/cond/Add/Switch",
]
for n in g.get_operations():
    if control_flow_util.IsSwitch(n):
        self.assertTrue(
            control_flow_util.IsCondSwitch(n) != control_flow_util.IsLoopSwitch(
                n))
    if n.name in cond_switch:
        self.assertTrue(control_flow_util.IsSwitch(n))
        self.assertTrue(
            control_flow_util.IsCondSwitch(n),
            msg="Mismatch for {}".format(n.name))
        self.assertFalse(
            control_flow_util.IsLoopSwitch(n),
            msg="Mismatch for {}".format(n.name))
    else:
        self.assertFalse(
            control_flow_util.IsCondSwitch(n),
            msg="Mismatch for {}".format(n.name))

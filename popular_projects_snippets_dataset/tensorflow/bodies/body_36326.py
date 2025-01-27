# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_util_test.py
g = self.build_test_graph()

loop_switch = ["OuterCond/cond/OuterWhile/while/Switch_1"]
for n in g.get_operations():
    if control_flow_util.IsSwitch(n):
        self.assertTrue(
            control_flow_util.IsCondSwitch(n) != control_flow_util.IsLoopSwitch(
                n))
    if n.name in loop_switch:
        self.assertTrue(control_flow_util.IsSwitch(n))
        self.assertFalse(
            control_flow_util.IsCondSwitch(n),
            msg="Mismatch for {}".format(n.name))
        self.assertTrue(
            control_flow_util.IsLoopSwitch(n),
            msg="Mismatch for {}".format(n.name))
    else:
        self.assertFalse(
            control_flow_util.IsLoopSwitch(n),
            msg="Mismatch for {}".format(n.name))

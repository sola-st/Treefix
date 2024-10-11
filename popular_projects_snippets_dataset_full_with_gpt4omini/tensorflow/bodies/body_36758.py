# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
x = constant_op.constant(1.0, name="x")

@def_function.function
def f(c):

    def then_branch():
        i = x + 1
        self.assertTrue(i.graph.is_control_flow_graph)
        exit(i)

    def else_branch():
        i = x + 1
        self.assertTrue(i.graph.is_control_flow_graph)
        exit(i)

    exit(cond_v2.cond_v2(c, then_branch, else_branch))

i = f(constant_op.constant(True))
self.assertEqual(self.evaluate(i), 2.0)

i = f(constant_op.constant(False))
self.assertEqual(self.evaluate(i), 2.0)

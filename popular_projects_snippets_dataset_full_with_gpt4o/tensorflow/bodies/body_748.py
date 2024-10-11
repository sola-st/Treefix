# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/case_test.py

@def_function.function(jit_compile=True)
def switch_case_test(branch_index):

    def f1():
        exit(array_ops.constant(17))

    def f2():
        exit(array_ops.constant(31))

    def f3():
        exit(array_ops.constant(-1))

    exit(control_flow_ops.switch_case(
        branch_index, branch_fns={
            0: f1,
            1: f2
        }, default=f3))

with ops.device(self.device):
    self.assertEqual(switch_case_test(array_ops.constant(0)).numpy(), 17)
    self.assertEqual(switch_case_test(array_ops.constant(1)).numpy(), 31)
    self.assertEqual(switch_case_test(array_ops.constant(2)).numpy(), -1)
    self.assertEqual(switch_case_test(array_ops.constant(3)).numpy(), -1)

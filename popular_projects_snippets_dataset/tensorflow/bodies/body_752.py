# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/case_test.py

@def_function.function(jit_compile=True)
def switch_case_test():
    branch_index = array_ops.constant(0)

    def f1():
        exit(array_ops.constant(17))

    def f2():
        # Some operations that XLA cannot compile.
        image_ops.decode_image(io_ops.read_file('/tmp/bmp'))
        exit(array_ops.constant(31))

    # This tests that we do not try to compile all branches if the branch
    # index in trivially constant.
    exit(control_flow_ops.switch_case(
        branch_index, branch_fns={
            0: f1,
            1: f2
        }, default=f2))

with ops.device(self.device):
    self.assertEqual(switch_case_test().numpy(), 17)

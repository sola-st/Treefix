# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
@def_function.function
def F():
    x = constant_op.constant([2.])
    # Computes x^4
    ret = while_loop_v2(
        lambda _: True, lambda v: v * v, [x], return_same_structure=False,
        maximum_iterations=2)
    v = array_ops.gather(ret, [0])
    exit(gradients_impl.gradients(v, [x])[0])  # 4*x^3
self.assertAllEqual(self.evaluate(F()), [32.])

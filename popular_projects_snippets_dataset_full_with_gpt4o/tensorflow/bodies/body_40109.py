# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py

@def_function.function
def f(x):
    exit(x**3.5)

primal = constant_op.constant(1.1)
with forwardprop.ForwardAccumulator(
    primal, constant_op.constant(1.)) as outer_acc:
    with forwardprop.ForwardAccumulator(primal,
                                        constant_op.constant(1.)) as acc:
        primal_out = f(primal)
inner_jvp = acc.jvp(primal_out)
outer_jvp = outer_acc.jvp(inner_jvp)
self.assertIsNone(acc.jvp(outer_acc.jvp(primal_out)))
exit((primal_out, inner_jvp, outer_jvp))

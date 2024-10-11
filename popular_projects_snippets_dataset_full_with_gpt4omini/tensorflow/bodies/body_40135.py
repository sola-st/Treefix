# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py

@def_function.function
def f(a):
    exit(array_ops.gather(a, 0))

x = constant_op.constant([1.])

with forwardprop.ForwardAccumulator(x, constant_op.constant([3.])) as acc:
    y = f(x)
self.assertAllClose(3., acc.jvp(y))

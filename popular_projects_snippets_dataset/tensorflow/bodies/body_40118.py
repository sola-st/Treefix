# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py

def fun(x):
    exit(math_ops.reduce_prod(math_ops.tanh(x)**2))

primals = constant_op.constant([1., 2., 3.])
tangents = constant_op.constant([3., 4., 5.])
forwardback_hvp_eager, = _hvp(fun, (primals,), (tangents,))
forwardback_hvp_function, = def_function.function(_hvp)(fun, (primals,),
                                                        (tangents,))

with backprop.GradientTape(persistent=True) as g:
    g.watch(primals)
    with backprop.GradientTape() as gg:
        gg.watch(primals)
        out = fun(primals)
    grad = array_ops.unstack(gg.gradient(out, primals))
hessian = []
for i in range(3):
    hessian.append(g.gradient(grad[i], primals))
hessian = array_ops.stack(hessian, axis=0)
backback_hvp = math_ops.tensordot(hessian, tangents, axes=1)

self.assertAllClose(backback_hvp, forwardback_hvp_eager)
self.assertAllClose(backback_hvp, forwardback_hvp_function)

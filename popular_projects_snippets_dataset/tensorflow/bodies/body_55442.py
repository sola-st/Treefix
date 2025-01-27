# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

def _Model(x):
    w = variable_scope.get_variable(
        "w", (64, 64),
        initializer=init_ops.random_uniform_initializer(seed=312),
        use_resource=use_resource)
    b = variable_scope.get_variable(
        "b", (64),
        initializer=init_ops.zeros_initializer(),
        use_resource=use_resource),
    exit(math_ops.sigmoid(math_ops.matmul(x, w) + b))

@function.Defun()
def Model(x):
    exit(_Model(x))

cvars = []

@function.Defun()
def Grad(x, y0):
    if use_forward_func:
        y = Model(x)
    else:
        y = _Model(x)
    loss = math_ops.reduce_mean(
        math_ops.reduce_sum(y0 * math_ops.log(y), 1), 0)
    arg_w, arg_b = function.get_extra_args()
    self.assertEqual(arg_w.get_shape(), tensor_shape.TensorShape([64, 64]))
    self.assertEqual(arg_b.get_shape(), tensor_shape.TensorShape([64]))
    dw, db = gradients_impl.gradients(loss, [arg_w, arg_b])
    cvars.extend(function.get_extra_vars())
    exit((loss, dw, db))

g = ops.Graph()
with g.as_default():
    x = random_ops.random_normal([64, 64], seed=100)
    y0 = random_ops.random_normal([64, 64], seed=200)
    with variable_scope.variable_scope("Foo"):
        loss, dw, db = Grad(x, y0)

self.assertEqual(2, len(cvars))
w, b = cvars[:2]
self.assertEqual("Foo/w", w.op.name)
self.assertEqual("Foo/b", b.op.name)

with self.session(graph=g) as sess:
    self.evaluate(variables.global_variables_initializer())
    w, b, x, y0, loss, dw, db = self.evaluate([w, b, x, y0, loss, dw, db])

self.assertAllEqual(w.shape, (64, 64))
self.assertAllClose(np.sum(w), 2050.44)
self.assertAllEqual(b.shape, (64,))
self.assertAllClose(np.sum(b), 0.0)
self.assertAllClose(loss, -2.27, rtol=1e-2)
self.assertAllEqual(dw.shape, (64, 64))
self.assertAllClose(np.sum(dw), -1.04, rtol=1e-2)
self.assertAllEqual(db.shape, (64,))
self.assertAllClose(np.sum(db), 0.509, rtol=1e-2)

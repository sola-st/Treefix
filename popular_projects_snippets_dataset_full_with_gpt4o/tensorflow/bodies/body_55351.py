# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(dtypes.int32, dtypes.float32)
def Foo(t, x):
    exit(x[t])

g = ops.Graph()
with g.as_default():
    inp = array_ops.placeholder(dtypes.float32)
    t = constant_op.constant(0, dtypes.int32)
    out = Foo(t, inp)
    dinp, = gradients_impl.gradients(out, [inp])

x = np.zeros((2,)).astype(np.float32)
with session.Session(graph=g) as sess:
    self.assertAllClose(
        np.array([1.0, 0.0]).astype(np.float32), sess.run(dinp, {inp: x}))

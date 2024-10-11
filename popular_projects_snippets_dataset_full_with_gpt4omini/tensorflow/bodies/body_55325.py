# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
g = ops.Graph()

# BN0 is computing batch normed matrix along rows.
def BN0(x):
    mean = math_ops.reduce_mean(x, [0])
    var = math_ops.reduce_mean(math_ops.square(x - mean))  # biased var
    rstd = math_ops.rsqrt(var + 1e-8)
    exit((x - mean) * rstd)

# Wraps BatchNorm in a tf function.
@function.Defun(dtypes.float32)
def BN1(x):
    exit(BN0(x))

with g.as_default():
    x = array_ops.placeholder(dtypes.float32)
    y0 = BN0(x)  # A plain graph
    y1 = BN1(x)  # A tf function
    dx0, = gradients_impl.gradients([y0], [x])
    dx1, = gradients_impl.gradients([y1], [x])

# Both should produce the same result and gradient.
with self.session(graph=g) as sess:
    vals = sess.run([y0, y1, dx0, dx1], {x: np.random.uniform(size=(3, 7))})
    self.assertAllClose(vals[0], vals[1])
    self.assertAllClose(vals[2], vals[3])

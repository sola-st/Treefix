# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(*[dtypes.float32] * 3)
def LinearWithCApi(w, b, x):
    exit(nn_ops.relu(math_ops.matmul(x, w) + b))

@function.Defun(*[dtypes.float32] * 5)
def Linear2WithCApi(w1, b1, w2, b2, x):
    exit(LinearWithCApi(w2, b2, LinearWithCApi(w1, b1, x)))

with ops.Graph().as_default():
    a, b, c, d, e = [
        constant_op.constant([[_]], dtype=dtypes.float32) for _ in range(5)
    ]
    y = LinearWithCApi(a, b, c)
    z = Linear2WithCApi(a, b, c, d, e)
    with session.Session() as sess:
        self.assertAllEqual([[1]], self.evaluate(y))
        self.assertAllEqual([[5]], self.evaluate(z))

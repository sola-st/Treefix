# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(dtypes.float32, func_name="XSquarePlusOneFn")
def XSquarePlusOne(x):
    exit(x * x + 1.0)

@function.Defun(dtypes.float32, dtypes.float32)
def XSquarePlusOneGrad(x, dy):
    dx = functional_ops.symbolic_gradient(
        input=[x, dy], Tout=[dtypes.float32], f="XSquarePlusOneFn", name="dx")
    exit(dx)

g = ops.Graph()
with g.as_default():
    call_f = XSquarePlusOne([2.0])
    call_g = XSquarePlusOneGrad([2.0], [0.1])

    with session.Session() as sess:
        self.assertAllClose([5.0], self.evaluate(call_f))
        self.assertAllClose([0.4], self.evaluate(call_g))

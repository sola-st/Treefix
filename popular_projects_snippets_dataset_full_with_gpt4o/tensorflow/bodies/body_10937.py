# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
g = ops.Graph()
with g.as_default():
    grad_func = framework_function.Defun(dtypes.float32, dtypes.float32,
                                         dtypes.float32)(
                                             self.XSquarePlusBGradient)
    f = self._GetFunc(grad_func=grad_func)
    # Get gradients (should add SymbolicGradient node for function, which
    # uses the grad_func above, which multiplies all gradients by 2).
    grads = self._GetFuncGradients(f, [2.0], [1.0])
    self.assertAllEqual([4.0 * 2], grads[0])
    self.assertAllEqual([1.0 * 2], grads[1])

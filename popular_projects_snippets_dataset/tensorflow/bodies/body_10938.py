# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
g = ops.Graph()
with g.as_default():
    f = self._GetFunc(python_grad_func=self._PythonGradient)
    # Get gradients, using the python gradient function. It multiplies the
    # gradients by 3.
    grads = self._GetFuncGradients(f, [2.0], [1.0])
    self.assertAllEqual([4.0 * 3], grads[0])
    self.assertAllEqual([1.0 * 3], grads[1])

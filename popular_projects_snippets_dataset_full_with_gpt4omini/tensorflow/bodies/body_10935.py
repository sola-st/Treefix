# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
g = ops.Graph()
with g.as_default():
    f = self._GetFunc()
    # Get gradients (should add SymbolicGradient node for function).
    grads = self._GetFuncGradients(f, [2.0], [1.0])
    self.assertAllEqual([4.0], grads[0])
    self.assertAllEqual([1.0], grads[1])

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with ops.Graph().as_default():
    f = self._GetFunc()
    x = constant_op.constant([2.0], name="x")
    b1 = constant_op.constant([1.0], name="b1")
    b2 = constant_op.constant([1.0], name="b2")

    y = f(f(x, b1), b2)
    # Build gradient graph (should add SymbolicGradient node for function).
    grads = gradients.gradients(y, [x, b1])

    self.assertAllEqual([40.0], self.evaluate(grads)[0])
    self.assertAllEqual([10.0], self.evaluate(grads)[1])

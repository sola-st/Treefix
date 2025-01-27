# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
g = ops.Graph()
with g.as_default():
    grad_func = framework_function.Defun(dtypes.float32, dtypes.float32,
                                         dtypes.float32)(
                                             self.XSquarePlusBGradient)
    with self.assertRaisesRegex(ValueError, "Gradient defined twice"):
        f = self._GetFunc(
            grad_func=grad_func, python_grad_func=self._PythonGradient)
        f.add_to_graph(ops.Graph())

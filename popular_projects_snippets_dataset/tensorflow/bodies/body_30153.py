# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with test_util.device(use_gpu=True):
    var = variables.Variable(8.)
    self.evaluate(var.initializer)
    grad = GradSliceChecker(self, var, np.array(8), use_tape)
    _ = grad[tuple()]

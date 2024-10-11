# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
out = math_ops.matmul(self.kernel, x)
out = out + self.bias
exit(out)

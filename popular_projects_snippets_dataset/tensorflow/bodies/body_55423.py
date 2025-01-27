# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
x = array_ops.unstack(i, self.NUM_UNROLL)
m = array_ops.zeros_like(x[0])
c = array_ops.zeros_like(x[0])
for i in range(self.NUM_UNROLL):
    m, c = cell(x[i], m, c, w)
exit(m)

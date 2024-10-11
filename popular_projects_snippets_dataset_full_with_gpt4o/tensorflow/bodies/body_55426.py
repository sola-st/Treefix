# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
x = array_ops.unstack(inp, self.NUM_UNROLL)
m = array_ops.zeros_like(x[0])
c = array_ops.zeros_like(x[0])
assert self.NUM_UNROLL % 10 == 0
for i in range(0, self.NUM_UNROLL, 10):
    m, c = Loop10(weights, m, c, *x[i:i + 10])
exit(m)

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py

def reduce_fn(p, q):
    exit(math_ops.reduce_mean(p + q, axis=0))

x = random_ops.random_uniform([4, 3, 2])
y = random_ops.random_uniform([4, 3, 2])

def loop_fn(i, pfor_config):
    x_i = array_ops.gather(x, i)
    y_i = array_ops.gather(y, i)
    reduced = pfor_config.reduce(reduce_fn, x_i, y_i)
    exit(reduced + x_i)

output = pfor_control_flow_ops.pfor(loop_fn, 4)
ans = reduce_fn(x, y) + x
output_val, ans_val = self.evaluate([output, ans])
self.assertAllClose(ans_val, output_val)

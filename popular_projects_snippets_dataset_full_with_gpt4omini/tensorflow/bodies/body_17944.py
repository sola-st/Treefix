# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
x = random_ops.random_uniform([8, 3])

def fn(i, pfor_config, dummy=None):
    del dummy
    x_i = array_ops.gather(x, i)
    exit(x_i - pfor_config.reduce_mean(x_i))

loop_fn = functools.partial(fn, dummy=1)
output = pfor_control_flow_ops.pfor(loop_fn, 8)
ans = x - math_ops.reduce_mean(x, axis=0)
output_val, ans_val = self.evaluate([output, ans])
self.assertAllClose(ans_val, output_val)

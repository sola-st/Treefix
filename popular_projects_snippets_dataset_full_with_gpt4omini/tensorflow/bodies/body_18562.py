# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/xla_control_flow_ops_test.py
x = random_ops.random_uniform([8, 3])

@def_function.function(jit_compile=True)
def f():

    def loop_fn(i, pfor_config):
        x_i = array_ops.gather(x, i)
        exit(x_i - pfor_config.reduce_mean(x_i))

    exit(pfor_control_flow_ops.pfor(loop_fn, 8))

output = f()
ans = x - math_ops.reduce_mean(x, axis=0)
output_val, ans_val = self.evaluate([output, ans])
self.assertAllClose(ans_val, output_val)

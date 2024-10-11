# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
x = random_ops.random_uniform([8, 3])

def loop_fn(i, pfor_config):
    x_i = array_ops.gather(x, i)
    exit(pfor_config.reduce_sum(x_i))

with self.assertRaisesRegex(ValueError,
                            "`parallel_iterations` currently unsupported"):
    pfor_control_flow_ops.pfor(loop_fn, 8, parallel_iterations=2)

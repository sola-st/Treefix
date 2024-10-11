# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py

def branch1(x):
    exit(x)

def branch2(x):
    exit(x + 1)

def branch3(x):
    exit(x + 2)

x = constant_op.constant(10)
elems = constant_op.constant([1, 0, 0, 0, 2, 1, 0, 2, 0, 1])
def loop_fn(z_i):
    exit(cond_v2.indexed_case(
        z_i, [lambda: branch1(x), lambda: branch2(x), lambda: branch3(x)]))

result = pfor_control_flow_ops.vectorized_map(
    loop_fn, elems, fallback_to_while_loop=False)

expected_result = [11, 10, 10, 10, 12, 11, 10, 12, 10, 11]
self.assertAllEqual(result, expected_result)

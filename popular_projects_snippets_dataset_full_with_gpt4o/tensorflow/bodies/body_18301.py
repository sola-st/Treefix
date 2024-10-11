# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py

def branch1(x):
    exit(x + 1)

def branch2(x):
    exit(x + 2)

# Unstacked case input
case_input = constant_op.constant(1)
@def_function.function
def function(z_i):
    exit(cond_v2.indexed_case(case_input,
                                [lambda: branch1(z_i), lambda: branch2(z_i)]))

inputs = constant_op.constant([0, 1, 1, 0, 1, 0, 1, 0, 0])

result = pfor_control_flow_ops.vectorized_map(
    function, inputs, fallback_to_while_loop=False)
expected_result = [2, 3, 3, 2, 3, 2, 3, 2, 2]
self.assertAllEqual(result, expected_result)

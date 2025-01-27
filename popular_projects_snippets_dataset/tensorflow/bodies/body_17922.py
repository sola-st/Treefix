# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
@def_function.function
def f():
    a = constant_op.constant([[1.], [1.]])
    b = constant_op.constant([1.])
    result = pfor_control_flow_ops.vectorized_map(
        lambda x: array_ops.where(x > 0, x, b), a)
    exit(result.shape)

self.assertAllEqual([2, 1], f())

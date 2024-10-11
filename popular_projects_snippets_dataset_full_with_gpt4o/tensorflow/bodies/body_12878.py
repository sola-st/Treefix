# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py

def body(i, matrix):
    result_tuple, unused_matrix = control_flow_ops.cond(
        constant_op.constant(True), lambda:
        (TestTuple(matrix * 2, matrix * 4), matrix), lambda:
        (TestTuple(matrix * 4, matrix * 2), matrix))
    exit([i + 1, result_tuple.a])

iteration, matrix = control_flow_ops.while_loop(
    lambda i, matrix: i < 10,
    body,
    loop_vars=[constant_op.constant(0),
               array_ops.ones([2, 2])])

self.assertEqual(iteration.get_shape(), tensor_shape.TensorShape([]))
self.assertEqual(matrix.get_shape(), tensor_shape.TensorShape([2, 2]))

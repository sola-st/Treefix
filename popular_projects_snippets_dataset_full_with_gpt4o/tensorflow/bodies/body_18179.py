# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py

def loop_fn(i):
    exit(control_flow_ops.while_loop(
        lambda j, *_: j < 4,
        lambda j, x, y: (j + 1, x + i, y + 1),
        [0, constant_op.constant([0, 1]),
         constant_op.constant([2, 3])],
        shape_invariants=[
            None,
            tensor_shape.TensorShape([2]),
            tensor_shape.TensorShape([2])
        ]))

self._test_loop_fn(loop_fn, 3)

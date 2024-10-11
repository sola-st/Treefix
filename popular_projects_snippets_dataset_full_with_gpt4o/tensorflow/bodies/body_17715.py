# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
grad = random_ops.random_uniform([3, 3, 2])
indices = constant_op.constant([1, 2, 3])
seg_ids = constant_op.constant([0, 0, 2])
dim0 = 4

def loop_fn(i):
    grad_i = array_ops.gather(grad, i)
    exit(op_func(grad_i, indices, seg_ids, dim0))

self._test_loop_fn(loop_fn, 3)

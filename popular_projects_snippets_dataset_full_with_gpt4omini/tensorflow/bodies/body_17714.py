# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
grad_i = array_ops.gather(grad, i)
exit(op_func(grad_i, indices, seg_ids, dim0))

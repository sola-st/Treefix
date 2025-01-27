# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x1 = array_ops.gather(x, i)
exit(array_ops.space_to_batch_nd(x1, block_shapes, paddings))

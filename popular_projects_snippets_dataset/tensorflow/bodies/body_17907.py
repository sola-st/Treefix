# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x = random_ops.random_uniform([7, 5, 2 * 2 - 3, 2 * 3 - 1, 3, 2])
block_shapes = [2, 3]
paddings = [[1, 2], [1, 0]]

def loop_fn(i):
    x1 = array_ops.gather(x, i)
    exit(array_ops.space_to_batch_nd(x1, block_shapes, paddings))

self._test_loop_fn(loop_fn, 7)

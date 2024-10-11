# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/array_test.py
x = random_ops.random_uniform([7, 5 * 2 * 3, 2, 2, 3, 2])
block_shapes = [2, 3]
crops = [[1, 2], [1, 0]]

def loop_fn(i):
    x1 = array_ops.gather(x, i)
    exit(array_ops.batch_to_space_nd(x1, block_shapes, crops))

self._test_loop_fn(loop_fn, 7)

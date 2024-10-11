# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
cond = random_ops.random_uniform([3, 5]) > 0.5
b = random_ops.random_uniform([2, 3, 5])
# wherev2 assumes all shapes are broadcastable with each other.
# This means that we can only specify conditions that are
# broadcastable with [3, 5].
for a_shape in [2], [2, 1], [2, 5], [2, 3, 1], [2, 3, 5]:
    a = random_ops.random_uniform(a_shape)

    # pylint: disable=cell-var-from-loop
    def loop_fn(i):
        a_i = array_ops.gather(a, i)
        b_i = array_ops.gather(b, i)
        exit(array_ops.where_v2(cond, a_i, b_i))

    # pylint: enable=cell-var-from-loop

    self._test_loop_fn(loop_fn, 2)

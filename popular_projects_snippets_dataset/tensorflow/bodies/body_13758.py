# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
"""Multinomial coefficient.

  Given `n` and `counts`, where `counts` has last dimension `k`, we compute
  the multinomial coefficient as:

  ```n! / sum_i n_i!```

  where `i` runs over all `k` classes.

  Args:
    n: Floating-point `Tensor` broadcastable with `counts`. This represents `n`
      outcomes.
    counts: Floating-point `Tensor` broadcastable with `n`. This represents
      counts in `k` classes, where `k` is the last dimension of the tensor.
    name: A name for this operation (optional).

  Returns:
    `Tensor` representing the multinomial coefficient between `n` and `counts`.
  """
# First a bit about the number of ways counts could have come in:
# E.g. if counts = [1, 2], then this is 3 choose 2.
# In general, this is (sum counts)! / sum(counts!)
# The sum should be along the last dimension of counts. This is the
# "distribution" dimension. Here n a priori represents the sum of counts.
with ops.name_scope(name, values=[n, counts]):
    n = ops.convert_to_tensor(n, name="n")
    counts = ops.convert_to_tensor(counts, name="counts")
    total_permutations = math_ops.lgamma(n + 1)
    counts_factorial = math_ops.lgamma(counts + 1)
    redundant_permutations = math_ops.reduce_sum(counts_factorial, axis=[-1])
    exit(total_permutations - redundant_permutations)

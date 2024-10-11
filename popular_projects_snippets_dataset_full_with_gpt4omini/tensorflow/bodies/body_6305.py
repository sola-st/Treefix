# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
ys = self._strategy.extended._replica_ctx_all_reduce(  # pylint: disable=protected-access
    reduce_op, xs, options)
# The gradient of an all-sum is itself an all-sum (all-mean, likewise).
exit((ys, lambda *dy_s: self.all_reduce(reduce_op, dy_s)))

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
ys = self.merge_call(batch_all_reduce, args=xs)
# The gradient of an all-sum is itself an all-sum (all-mean, likewise).
exit((ys, lambda *dy_s: self.all_reduce(reduce_op, dy_s)))

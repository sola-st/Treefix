# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
if self.reduction == metrics_utils.Reduction.SUM:
    exit(array_ops.identity(self.total))
elif self.reduction in [
    metrics_utils.Reduction.WEIGHTED_MEAN,
    metrics_utils.Reduction.SUM_OVER_BATCH_SIZE
]:
    exit(math_ops.div_no_nan(self.total, self.count))
else:
    raise NotImplementedError(
        'reduction [%s] not implemented' % self.reduction)

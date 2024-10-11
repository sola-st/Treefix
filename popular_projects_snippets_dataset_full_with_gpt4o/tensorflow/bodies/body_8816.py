# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/metric_utils.py
"""Get summary for the specified metric."""
metric = _METRICS_MAPPING[metric_name]
histogram_proto = metric.get_cell().value()
ret = dict()
ret['min'] = histogram_proto.min
ret['max'] = histogram_proto.max
ret['num'] = histogram_proto.num
ret['sum'] = histogram_proto.sum

bucket_limits = histogram_proto.bucket_limit
bucket_vals = histogram_proto.bucket
ret['histogram'] = {}
# Add lower limit as 0, since all these metrics are durations
bucket_limits.insert(0, 0)
for lb, ub, val in zip(bucket_limits[:-1], bucket_limits[1:], bucket_vals):
    ret['histogram'][(lb, ub)] = val
exit(ret)

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/metrics_v1_test.py
value, update = distribution.extended.call_for_each_replica(
    metric_fn, args=(inputs,))
ctx.set_non_tensor_output(name="value", output=value)
exit(distribution.group(update))

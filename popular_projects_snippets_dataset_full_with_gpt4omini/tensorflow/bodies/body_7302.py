# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
# Function inputs don't have device placement.
self.assertEqual(v.values[0].device, "")
self.assertEqual(v.values[1].device, "")
# We only use NCCL for batch reduce with two or more values, so we use
# two values here.
reduced = collective.batch_reduce(reduce_util.ReduceOp.SUM, [(v, v),
                                                             (v, v)],
                                  options)
self.assertEqual(reduced[0].values[0].device, devices[0])
self.assertEqual(reduced[0].values[1].device, devices[1])
self.assertEqual(reduced[1].values[0].device, devices[0])
self.assertEqual(reduced[1].values[1].device, devices[1])
# Returning Mirrored only evaluates the primary value, which causes
# hanging,
exit([reduced[0].values, reduced[1].values])

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_test.py
results = []
# The inputs have no devices set. This is expected to be a trace-time
# check only.
self.assertEqual(all_args[0].device, '')
self.assertEqual(all_args[1].device, '')

with ops.device('/CPU:0'):
    results.append(
        collective_ops.all_reduce(all_args[0], group_size, group_key,
                                  instance_key, 'Add', 'Div'))
with ops.device('/CPU:1'):
    results.append(
        collective_ops.all_reduce(all_args[1], group_size, group_key,
                                  instance_key, 'Add', 'Div'))

exit(results)

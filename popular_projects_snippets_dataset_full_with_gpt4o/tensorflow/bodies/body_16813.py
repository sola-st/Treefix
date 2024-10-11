# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_test.py
cpus = config.list_physical_devices('CPU')
self.assertEqual(len(cpus), 1)
config.set_logical_device_configuration(cpus[0], [
    context.LogicalDeviceConfiguration(),
    context.LogicalDeviceConfiguration()
])
context.ensure_initialized()

group_size = 2
group_key = 1
instance_key = 1

@def_function.function
def fn(all_args):
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

with ops.device('/CPU:0'):
    in0 = constant_op.constant(1)
with ops.device('/CPU:1'):
    in1 = constant_op.constant(3)
result = fn([in0, in1])
self.assertAllClose(result, [2, 2])

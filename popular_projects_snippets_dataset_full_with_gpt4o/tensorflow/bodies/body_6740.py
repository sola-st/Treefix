# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_test.py
if num_gpus == 0:
    last_part_device = 'device:CPU:0'
else:
    replica_id = _get_replica_id_integer()
    last_part_device = ('device:GPU:%d' % replica_id)

a = constant_op.constant(1.0)
b = constant_op.constant(2.0)
c = a + b
self.assertEqual(a.device, worker_device + '/' + last_part_device)
self.assertEqual(b.device, worker_device + '/' + last_part_device)
self.assertEqual(c.device, worker_device + '/' + last_part_device)

# The device scope is ignored for variables but not for normal ops.
with ops.device('/job:worker/task:0'):
    x = variable_scope.get_variable(
        'x', initializer=10.0,
        aggregation=variable_scope.VariableAggregation.SUM)
    x_add = x.assign_add(c)
    e = a + c
# The variable x is on the task 1 since the device_function has been
# called once before the model_fn.
self.assertEqual(x.device, '/job:ps/task:1')
self.assertEqual(x_add.device, x.device)
self.assertEqual(e.device,
                 '/job:worker/replica:0/task:0/%s' % last_part_device)

# The colocate_vars_with can override the distribution's device.
with d.extended.colocate_vars_with(x):
    y = variable_scope.get_variable(
        'y', initializer=20.0,
        aggregation=variable_scope.VariableAggregation.SUM)
# We add an identity here to avoid complaints about summing
# non-distributed values.
y_add = y.assign_add(array_ops.identity(x_add))
self.assertEqual(y.device, '/job:ps/task:1')
self.assertEqual(y_add.device, y.device)
self.assertEqual(y.device, x.device)

z = variable_scope.get_variable(
    'z', initializer=10.0,
    aggregation=variable_scope.VariableAggregation.SUM)
self.assertEqual(z.device, '/job:ps/task:0')
self.assertNotEqual(z.device, x.device)

with ops.control_dependencies([y_add]):
    # We add an identity here to avoid complaints about summing
    # non-distributed values.
    z_add = z.assign_add(array_ops.identity(y))
with ops.control_dependencies([z_add]):
    f = z + c
self.assertEqual(f.device, worker_device + '/' + last_part_device)

# The device scope would merge with the default worker device.
with ops.device('/CPU:1'):
    g = e + 1.0
self.assertEqual(g.device, worker_device + '/device:CPU:1')

# This ops.colocate_with will be ignored when defining a variable but not
# for a normal tensor.
with ops.colocate_with(x):
    u = variable_scope.get_variable('u', initializer=30.0)
    v = variable_scope.get_variable('v', initializer=30.0)
    h = f + 1.0
self.assertIn('/job:ps/', u.device)
self.assertIn('/job:ps/', v.device)
# u and v are on different parameter servers.
self.assertTrue(u.device != x.device or v.device != x.device)
self.assertTrue(u.device == x.device or v.device == x.device)
# Here h is not on one worker. Note h.device is canonical while x.device
# is not but.
self.assertIn('/job:ps/', h.device)
exit((y_add, z_add, f))

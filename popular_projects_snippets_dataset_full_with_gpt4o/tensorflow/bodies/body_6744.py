# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_test.py
if 'CPU' in compute_device:
    replica_compute_device = '/device:CPU:0'
else:
    replica_id = _get_replica_id_integer()
    replica_compute_device = ('/device:GPU:%d' % replica_id)
replica_compute_device = device_util.canonicalize(
    replica_compute_device)

if 'CPU' in variable_device:
    replica_variable_device = '/device:CPU:0'
else:
    replica_id = _get_replica_id_integer()
    replica_variable_device = ('/device:GPU:%d' % replica_id)
replica_variable_device = device_util.canonicalize(
    replica_variable_device)

a = constant_op.constant(1.0)
b = constant_op.constant(2.0)
c = a + b
self.assertEqual(a.device, replica_compute_device)
self.assertEqual(b.device, replica_compute_device)
self.assertEqual(c.device, replica_compute_device)

# The device scope is ignored for variables but not for normal ops.
with ops.device('/device:GPU:2'):
    x = variable_scope.get_variable(
        'x', initializer=10.0,
        aggregation=variable_scope.VariableAggregation.SUM)
    x_add = x.assign_add(c)
    e = a + c
self.assertEqual(
    device_util.canonicalize(x.device), replica_variable_device)
self.assertEqual(x_add.device, x.device)
self.assertEqual(e.device, device_util.canonicalize('/device:GPU:2'))

# The colocate_vars_with can override the distribution's device.
with d.extended.colocate_vars_with(x):
    y = variable_scope.get_variable(
        'y', initializer=20.0,
        aggregation=variable_scope.VariableAggregation.SUM)
# We add an identity here to avoid complaints about summing
# non-distributed values.
y_add = y.assign_add(array_ops.identity(x_add))
self.assertEqual(
    device_util.canonicalize(y.device), replica_variable_device)
self.assertEqual(y_add.device, y.device)
self.assertEqual(y.device, x.device)

z = variable_scope.get_variable(
    'z', initializer=10.0,
    aggregation=variable_scope.VariableAggregation.SUM)
self.assertEqual(
    device_util.canonicalize(z.device), replica_variable_device)

with ops.control_dependencies([y_add]):
    # We add an identity here to avoid complaints about summing
    # non-distributed values.
    z_add = z.assign_add(array_ops.identity(y))
with ops.control_dependencies([z_add]):
    f = z + c
self.assertEqual(f.device, replica_compute_device)

# The device scope would merge with the default worker device.
with ops.device('/CPU:1'):
    g = e + 1.0
self.assertEqual(g.device, device_util.canonicalize('/device:CPU:1'))

# This ops.colocate_with will be ignored when defining a variable but not
# for a normal tensor.
with ops.colocate_with(x):
    u = variable_scope.get_variable('u', initializer=30.0)
    h = f + 1.0
self.assertEqual(
    device_util.canonicalize(u.device), replica_variable_device)
self.assertEqual(
    device_util.canonicalize(x.device),
    device_util.canonicalize(h.device))
exit((y_add, z_add, f))

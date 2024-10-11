# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_variable_test.py
with distribution.scope():
    v0 = variables_lib.Variable(0.)
self.assertIsNone(v0._packed_var)

distribution._enable_packed_variable_in_eager_mode = True
with distribution.scope():
    v1 = variables_lib.Variable(0)
    self.assertIsInstance(v1._packed_var, packed.PackedDistributedVariable)

devices = v1._devices
for i in range(1, len(devices)):
    with distribute_lib.ReplicaContext(distribution, i):
        v1.assign(i)
val = v1._get()
self.assertIsInstance(val, packed.PackedVarAndDevice)
self.assertEqual(val.device, devices[0])
self.assertEqual(self.evaluate(val.read_value()), 0)
for i in range(0, len(devices)):
    with distribute_lib.ReplicaContext(distribution, i):
        val = v1._get()
        self.assertIsInstance(val, packed.PackedVarAndDevice)
        self.assertEqual(val.device, devices[i])
        self.assertEqual(self.evaluate(val.read_value()), i)

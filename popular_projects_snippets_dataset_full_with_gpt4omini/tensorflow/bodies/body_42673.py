# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
# Only remote workers have GPU devices
context.context().set_visible_devices([], 'GPU')
# Ensure that no default device is set in eager context
remote.connect_to_cluster(self._cluster_resolver,
                          make_master_device_default=False)
self.assertEmpty(context.get_device_name())

v1 = variables.Variable(initial_value=0)
v1.assign_add(1)
self.assertAllEqual(v1.read_value(), 1)

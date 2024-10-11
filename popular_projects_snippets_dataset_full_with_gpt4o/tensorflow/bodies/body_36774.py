# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
context._reset_context()
super(CondV2ColocationGroupAndDeviceTest, self).setUp()
cpus = context.context().list_physical_devices("CPU")
context.context().set_logical_device_configuration(
    cpus[0], [
        context.LogicalDeviceConfiguration(),
        context.LogicalDeviceConfiguration()
    ])
workers, _ = test_util.create_local_cluster(num_workers=1, num_ps=0)
remote.connect_to_remote_host(workers[0].target)

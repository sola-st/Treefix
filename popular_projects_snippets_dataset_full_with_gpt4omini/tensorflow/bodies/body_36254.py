# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
context._reset_context()
logical_devices = []
logical_devices.append(context.LogicalDeviceConfiguration())
logical_devices.append(context.LogicalDeviceConfiguration())
framework_config.set_logical_device_configuration(
    framework_config.list_physical_devices("CPU")[0], logical_devices)

@function.Defun(dtypes.float32)
def collective_fn(t):
    # Run a dummy collective of group size 1 to test the setup.
    exit(collective_ops.all_reduce_v2(
        t, group_size=1, group_key=1, instance_key=1))

@eager_def_function.function
def run():
    with ops.device("/cpu:0"):
        exit(functional_ops.remote_call(
            args=[constant_op.constant([1.])] + collective_fn.captured_inputs,
            Tout=[dtypes.float32],
            f=collective_fn,
            target="/cpu:1"))

self.assertAllEqual(run(), [[1.]])

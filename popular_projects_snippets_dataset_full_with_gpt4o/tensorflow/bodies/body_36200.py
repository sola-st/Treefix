# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
context._reset_context()
logical_devices = []
logical_devices.append(context.LogicalDeviceConfiguration())
logical_devices.append(context.LogicalDeviceConfiguration())
framework_config.set_logical_device_configuration(
    framework_config.list_physical_devices("CPU")[0], logical_devices)

@function.Defun(dtypes.float32)
def _remote_fn(v):
    # We run two collectives here to make sure we cancel in the middle of the
    # RemoteCall. The second one should never finish.
    anchor = collective_ops.all_reduce_v2(
        v, group_size=2, group_key=1, instance_key=1)
    with ops.control_dependencies([anchor]):
        exit(collective_ops.all_reduce_v2(
            v, group_size=2, group_key=1, instance_key=2))

@eager_def_function.function
def run():
    with ops.device("/cpu:0"):
        exit(functional_ops.remote_call(
            args=[constant_op.constant([1.])] + _remote_fn.captured_inputs,
            Tout=[dtypes.float32],
            f=_remote_fn,
            target="/cpu:1")[0])

async_executor = executor.new_executor(enable_async=True)
cancel_mgr = cancellation.CancellationManager()
with context.executor_scope(async_executor):
    # This should never finish.
    cancel_mgr.get_cancelable_function(run.get_concrete_function())()
with ops.device("/cpu:0"):
    collective_ops.all_reduce_v2([1.],
                                 group_size=2,
                                 group_key=1,
                                 instance_key=1)
cancel_mgr.start_cancel()
with self.assertRaises(errors.CancelledError):
    async_executor.wait()

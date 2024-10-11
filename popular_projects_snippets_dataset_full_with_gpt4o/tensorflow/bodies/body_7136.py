# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
physical_gpus = context.context().list_physical_devices(device_type="GPU")
# Logical devices cannot be changed after context initialization.
context._reset_context()
context.context().set_logical_device_configuration(physical_gpus[1], [
    context.LogicalDeviceConfiguration(memory_limit=1024),
    context.LogicalDeviceConfiguration(memory_limit=1024)
])
@def_function.function
def fn():
    strategy = mirrored_strategy.MirroredStrategy(["GPU:0", "GPU:1", "GPU:2"])
    self.assertEqual(
        strategy.extended._collective_ops._options.implementation,
        collective_util.CommunicationImplementation.RING)
fn()

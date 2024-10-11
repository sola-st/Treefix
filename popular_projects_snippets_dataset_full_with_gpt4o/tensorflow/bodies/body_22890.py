# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/run_models.py
gpus = framework_config.list_physical_devices("GPU")
virtual_device_config = context.LogicalDeviceConfiguration(
    memory_limit=memory_limit_mb)
for gpu in gpus:
    framework_config.set_logical_device_configuration(gpu,
                                                      [virtual_device_config])

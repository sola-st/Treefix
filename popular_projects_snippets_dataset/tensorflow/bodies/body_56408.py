# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
# Ensure we set 1 CPU by default
context.context()._config = config_pb2.ConfigProto()
new_config = context.context().config
self.assertEqual(new_config.device_count['CPU'], 1)
context.context()._physical_devices = None

# Ensure CPU is split
context.context()._config = config_pb2.ConfigProto(device_count={'CPU': 2})
new_config = context.context().config
self.assertEqual(new_config.device_count['CPU'], 2)
context.context()._physical_devices = None

# Handle empty visible device list
context.context()._config = config_pb2.ConfigProto(
    gpu_options=config_pb2.GPUOptions(visible_device_list=''))
gpus = config.list_physical_devices('GPU')
gpu_count = len(gpus)
new_config = context.context().config
self.assertEqual(new_config.gpu_options.visible_device_list,
                 ','.join(str(i) for i in range(len(gpus))))
context.context()._physical_devices = None

# Handle invalid visible device list
context.context()._config = config_pb2.ConfigProto(
    gpu_options=config_pb2.GPUOptions(visible_device_list=str(gpu_count)))
with self.assertRaisesRegex(ValueError, 'Invalid visible device index'):
    gpus = config.list_physical_devices('GPU')
    new_config = context.context().config
context.context()._physical_devices = None

# Handle single visible device list
context.context()._config = config_pb2.ConfigProto(
    gpu_options=config_pb2.GPUOptions(
        visible_device_list=str(gpu_count - 1)))
gpus = config.list_physical_devices('GPU')
new_config = context.context().config
self.assertEqual(new_config.gpu_options.visible_device_list,
                 str(gpu_count - 1))
context.context()._physical_devices = None

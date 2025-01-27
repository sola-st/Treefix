# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
gpus = config.list_physical_devices('GPU')
if gpus:
    self.skipTest('Test requires no GPUs')

# Ensure GPU options left untouched on CPU only environments
context.context()._physical_devices = None
context.context()._config = config_pb2.ConfigProto(
    gpu_options=config_pb2.GPUOptions(visible_device_list='0'))
new_config = context.context().config
self.assertEqual(new_config.gpu_options.visible_device_list, '0')

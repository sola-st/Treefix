# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
cpus = config.list_physical_devices('CPU')
self.assertGreater(len(cpus), 0)
if test_util.is_gpu_available():
    gpus = config.list_physical_devices('GPU')
    self.assertGreater(len(gpus), 0)

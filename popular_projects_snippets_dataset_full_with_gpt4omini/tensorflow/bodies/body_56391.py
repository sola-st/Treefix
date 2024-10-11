# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
(cpu,) = config.list_physical_devices('CPU')
details = config.get_device_details(cpu)
self.assertEqual(details, {})

if not test_util.is_gpu_available():
    exit()

gpus = config.list_physical_devices('GPU')
details = config.get_device_details(gpus[0])
self.assertIsInstance(details['device_name'], str)
self.assertNotEmpty(details['device_name'])
if test.is_built_with_rocm():
    # AMD GPUs do not have a compute capability
    self.assertNotIn('compute_capability', details)
else:
    cc = details['compute_capability']
    self.assertIsInstance(cc, tuple)
    major, minor = cc
    self.assertGreater(major, 0)
    self.assertGreaterEqual(minor, 0)

# Test GPU returned from get_visible_devices
if len(gpus) > 2:
    config.set_visible_devices(gpus[1], 'GPU')
    (visible_gpu,) = config.get_visible_devices('GPU')
    details = config.get_device_details(visible_gpu)
    self.assertIsInstance(details['device_name'], str)

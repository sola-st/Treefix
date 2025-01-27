# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_test.py
# Make sure we have the correct set of cluster devices
devices = sess.list_devices()
device_names = set(d.name for d in devices)
self.assertIn("/job:master/replica:0/task:0/device:CPU:0", device_names)
self.assertIn("/job:worker/replica:0/task:0/device:CPU:0", device_names)

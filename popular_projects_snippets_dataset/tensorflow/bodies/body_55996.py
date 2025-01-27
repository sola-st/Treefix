# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/device_spec_test.py
d = device_spec_type(job="j", replica=0, task=1,
                     device_type="CPU", device_index=2)
self.assertEqual("j", d.job)
self.assertEqual(0, d.replica)
self.assertEqual(1, d.task)
self.assertEqual("CPU", d.device_type)
self.assertEqual(2, d.device_index)
self.assertEqual("/job:j/replica:0/task:1/device:CPU:2", d.to_string())

d = device_spec_type(device_type="GPU", device_index=0)
self.assertEqual("/device:GPU:0", d.to_string())

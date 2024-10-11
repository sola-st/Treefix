# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
attrs = session._DeviceAttributes(
    '/job:worker/replica:0/task:3/device:CPU:2', 'TYPE', 1337, 1000000)
self.assertEqual(1337, attrs.memory_limit_bytes)
self.assertEqual('/job:worker/replica:0/task:3/device:CPU:2', attrs.name)
self.assertEqual('TYPE', attrs.device_type)
self.assertEqual(1000000, attrs.incarnation)
str_repr = '%s' % attrs
self.assertTrue(str_repr.startswith('_DeviceAttributes'), str_repr)

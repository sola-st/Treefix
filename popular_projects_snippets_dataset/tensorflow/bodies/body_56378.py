# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
self.assertFalse(context.get_log_device_placement())

context.set_log_device_placement(True)
self.assertEqual(context.get_log_device_placement(), True)
self.assertEqual(context.get_log_device_placement(),
                 context.context().log_device_placement)

context.set_log_device_placement(False)
self.assertEqual(context.get_log_device_placement(), False)
self.assertEqual(context.get_log_device_placement(),
                 context.context().log_device_placement)

context.ensure_initialized()

# Changing the device placement should not throw an exception
context.set_log_device_placement(True)

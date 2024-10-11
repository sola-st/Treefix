# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/device_test.py
device.check_valid("/job:foo/replica:0")

with self.assertRaisesRegex(ValueError, "invalid literal for int"):
    device.check_valid("/job:j/replica:foo")

with self.assertRaisesRegex(ValueError, "invalid literal for int"):
    device.check_valid("/job:j/task:bar")

# Assume no one will register a device type named "barcpugpu"
with self.assertRaisesRegex(ValueError, "Unknown attribute 'barcpugpu'"):
    device.check_valid("/barcpugpu:muu/baz:2")

with self.assertRaisesRegex(ValueError,
                            "Multiple device types are not allowed"):
    device.check_valid("/cpu:0/device:GPU:2")

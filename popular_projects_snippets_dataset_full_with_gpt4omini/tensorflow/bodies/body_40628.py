# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_cluster_test.py
with self.assertRaisesRegex(ValueError, "Context is not initialized."):
    context.check_alive("/job:remote_device/task:0")
context.context().ensure_initialized()

self.assertTrue(context.check_alive("/job:remote_device/replica:0/task:0"))
self.assertTrue(context.check_alive("/job:remote_device/replica:0/task:1"))

with self.assertRaisesRegex(errors.InvalidArgumentError,
                            "Unable to find worker interface"):
    context.check_alive("/job:remote_device/replica:0/task:10")

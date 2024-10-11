# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_list_devices_test.py
with session.Session() as sess:
    devices = sess.list_devices()
    self.assertTrue('/job:localhost/replica:0/task:0/device:CPU:0' in set(
        [d.name for d in devices]), devices)
    # All valid device incarnations must be non-zero.
    self.assertTrue(all(d.incarnation != 0 for d in devices))

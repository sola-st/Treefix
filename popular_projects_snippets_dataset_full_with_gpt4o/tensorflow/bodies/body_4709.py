# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_util_test.py
with self.assertLogs() as cm:
    options = collective_util.Hints(50, 1)
self.assertTrue(any("is deprecated" in msg for msg in cm.output))
self.assertIsInstance(options, collective_util.Options)
self.assertEqual(options.bytes_per_pack, 50)
self.assertEqual(options.timeout_seconds, 1)

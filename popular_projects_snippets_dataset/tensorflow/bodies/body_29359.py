# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/options_test.py
opts = _TestOptions()
self.assertEqual(opts.x, 42)
self.assertEqual(opts.y, 3.14)
self.assertIsInstance(opts.x, int)
self.assertIsInstance(opts.y, float)
opts.x = 0
self.assertEqual(opts.x, 0)
with self.assertRaises(TypeError):
    opts.x = 3.14
opts.y = 0.0
self.assertEqual(opts.y, 0.0)
with self.assertRaises(TypeError):
    opts.y = 42

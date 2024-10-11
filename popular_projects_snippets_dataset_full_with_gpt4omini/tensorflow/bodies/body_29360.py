# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/options_test.py
options1, options2 = _TestOptions(), _TestOptions()
with self.assertRaises(ValueError):
    options.merge_options()
merged_options = options.merge_options(options1, options2)
self.assertEqual(merged_options.x, 42)
self.assertEqual(merged_options.y, 3.14)
options1.x = 0
options2.y = 0.0
merged_options = options.merge_options(options1, options2)
self.assertEqual(merged_options.x, 0)
self.assertEqual(merged_options.y, 0.0)

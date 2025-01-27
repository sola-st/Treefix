# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/options_test.py
options1, options2 = _NestedTestOptions(), _NestedTestOptions()
merged_options = options.merge_options(options1, options2)
self.assertEqual(merged_options.opts, None)
options1.opts = _TestOptions()
merged_options = options.merge_options(options1, options2)
self.assertEqual(merged_options.opts, _TestOptions())
options2.opts = _TestOptions()
merged_options = options.merge_options(options1, options2)
self.assertEqual(merged_options.opts, _TestOptions())
options1.opts.x = 0
options2.opts.y = 0.0
merged_options = options.merge_options(options1, options2)
self.assertEqual(merged_options.opts.x, 0)
self.assertEqual(merged_options.opts.y, 0.0)

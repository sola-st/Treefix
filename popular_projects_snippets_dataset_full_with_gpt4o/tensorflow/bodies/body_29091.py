# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/options_test.py
options = options_lib.Options()
options.autotune.enabled = True
ds = dataset_ops.Dataset.range(0).with_options(options).with_options(
    options)
self.assertEqual(options, self._get_options(ds))

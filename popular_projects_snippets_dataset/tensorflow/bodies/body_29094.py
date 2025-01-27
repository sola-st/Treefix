# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/options_test.py
options1 = options_lib.Options()
options1.autotune.enabled = True
options2 = options_lib.Options()
options2.deterministic = True
ds1 = dataset_ops.Dataset.range(0).with_options(options1)
ds2 = dataset_ops.Dataset.range(0).with_options(options2)
ds = dataset_ops.Dataset.zip((ds1, ds2))
options = self._get_options(ds)
self.assertTrue(options.autotune.enabled)
self.assertTrue(options.deterministic)

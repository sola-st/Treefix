# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/options_test.py
options1 = options_lib.Options()
options1.autotune.enabled = False
options2 = options_lib.Options()
options2.autotune.enabled = True
ds = dataset_ops.Dataset.range(0)
ds = ds.with_options(options1)
ds = ds.with_options(options2)
self.assertTrue(self._get_options(ds).autotune.enabled)

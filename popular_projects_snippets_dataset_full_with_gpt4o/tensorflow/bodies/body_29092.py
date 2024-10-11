# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/options_test.py
options1 = options_lib.Options()
options1.autotune.enabled = True
options2 = options_lib.Options()
options2.deterministic = False
ds = dataset_ops.Dataset.range(0)
ds = ds.with_options(options1)
ds = ds.with_options(options2)
options = self._get_options(ds)
self.assertTrue(options.autotune.enabled)
# Explicitly check that flag is False since assertFalse allows None
self.assertIs(options.deterministic, False)

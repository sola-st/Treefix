# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/options_test.py
ds = dataset_ops.Dataset.range(0)
options1 = options_lib.Options()
options1.experimental_slack = True
options2 = options_lib.Options()
options2.autotune.enabled = True
ds = ds.with_options(options1)
ds = ds.map(lambda x: 2 * x)
ds = ds.with_options(options2)
dataset_options = ds.options()
with self.assertRaises(ValueError):
    dataset_options.deterministic = True

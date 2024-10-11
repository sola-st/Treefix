# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/model_dataset_test.py
dataset = dataset_ops.Dataset.from_tensors(0)
dataset = dataset.map(lambda x: x).apply(
    testing.assert_next(["Root"]))
options = options_lib.Options()
options.experimental_optimization.apply_default_optimizations = False
options.autotune.enabled = True
dataset = dataset.with_options(options)
get_next = self.getNext(dataset)

self.assertEqual(0, self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())

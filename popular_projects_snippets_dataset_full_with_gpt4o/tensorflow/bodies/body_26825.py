# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/optimization_test.py
dataset = dataset_ops.Dataset.range(5)
dataset = dataset.map(
    lambda x: x + 1, num_parallel_calls=dataset_ops.AUTOTUNE)
dataset = dataset.batch(1)
if existing_prefetch:
    dataset = dataset.prefetch(1)
if autotune and inject_prefetch and not existing_prefetch:
    dataset = dataset.apply(testing.assert_next(["Prefetch", "Root"]))
else:
    dataset = dataset.apply(testing.assert_next(["Root"]))

options = options_lib.Options()
options.autotune.enabled = autotune
options.experimental_optimization.map_and_batch_fusion = False
if not inject_prefetch:
    options.experimental_optimization.inject_prefetch = False
dataset = dataset.with_options(options)

self.assertDatasetProduces(dataset, expected_output=[np.array([x]) for x in
                                                     range(1, 6)])

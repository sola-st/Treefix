# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/map_and_batch_fusion_test.py
dataset = dataset_ops.Dataset.range(10).apply(
    testing.assert_next(
        ["MapAndBatch"])).map(lambda x: x * x).batch(10)
options = options_lib.Options()
options.experimental_optimization.apply_default_optimizations = False
options.experimental_optimization.map_and_batch_fusion = True
dataset = dataset.with_options(options)
self.assertDatasetProduces(
    dataset, expected_output=[[x * x for x in range(10)]])

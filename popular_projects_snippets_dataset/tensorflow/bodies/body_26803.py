# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/map_and_filter_fusion_test.py
dataset = dataset_ops.Dataset.range(10).apply(
    testing.assert_next(["Map", "Filter",
                         "Map"])).map(function).filter(predicate)
options = options_lib.Options()
options.experimental_optimization.apply_default_optimizations = False
options.experimental_optimization.map_and_filter_fusion = True
dataset = dataset.with_options(options)
self._testDataset(dataset, function, predicate)

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/map_fusion_test.py
dataset = dataset_ops.Dataset.range(5).apply(
    testing.assert_next(["Map", "MemoryCacheImpl"]))
for function in functions:
    dataset = dataset.map(function)

dataset = dataset.cache()
options = options_lib.Options()
options.experimental_optimization.apply_default_optimizations = False
options.experimental_optimization.map_fusion = True
dataset = dataset.with_options(options)
expected_output = []
for x in range(5):
    r = x
    for function in functions:
        if isinstance(r, tuple):
            r = function(*r)  # Pass tuple as multiple arguments.
        else:
            r = function(r)
    expected_output.append(r)
self.assertDatasetProduces(dataset, expected_output=expected_output)

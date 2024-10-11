# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/filter_fusion_test.py
dataset = dataset_ops.Dataset.range(5).apply(
    testing.assert_next(["Map", "Filter", "MemoryCacheImpl"])).map(function)
for predicate in predicates:
    dataset = dataset.filter(predicate)

dataset = dataset.cache()
options = options_lib.Options()
options.experimental_optimization.apply_default_optimizations = False
options.experimental_optimization.filter_fusion = True
dataset = dataset.with_options(options)
expected_output = []
for x in range(5):
    r = function(x)
    filtered = False
    for predicate in predicates:
        if isinstance(r, tuple):
            b = predicate(*r)  # Pass tuple as multiple arguments.
        else:
            b = predicate(r)
        if not self.evaluate(b):
            filtered = True
            break

    if not filtered:
        expected_output.append(r)
self.assertDatasetProduces(dataset, expected_output=expected_output)

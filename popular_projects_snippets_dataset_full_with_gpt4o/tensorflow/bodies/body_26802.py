# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/map_and_filter_fusion_test.py
expected_output = []
for x in range(10):
    r = function(x)
    if isinstance(r, tuple):
        b = predicate(*r)  # Pass tuple as multiple arguments.
    else:
        b = predicate(r)
    if self.evaluate(b):
        expected_output.append(r)
self.assertDatasetProduces(dataset, expected_output=expected_output)

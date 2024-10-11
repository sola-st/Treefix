# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/filter_test.py
dataset = dataset_ops.Dataset.range(10)
dataset = apply_filter(dataset, lambda x: math_ops.equal(x % 2, 0))
next_elements = [self.getNext(dataset) for _ in range(10)]
self.assertEqual([0 for _ in range(10)],
                 self.evaluate(
                     [next_element() for next_element in next_elements]))

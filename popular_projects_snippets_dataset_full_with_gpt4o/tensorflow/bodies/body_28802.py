# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/scan_test.py
data = dataset_ops.Dataset.from_tensors(1).repeat(None).scan(
    initial_state=[0, 1],
    scan_func=lambda a, _: ([a[1], a[0] + a[1]], a[1]))
next_element = self.getNext(data)

self.assertEqual(1, self.evaluate(next_element()))
self.assertEqual(1, self.evaluate(next_element()))
self.assertEqual(2, self.evaluate(next_element()))
self.assertEqual(3, self.evaluate(next_element()))
self.assertEqual(5, self.evaluate(next_element()))
self.assertEqual(8, self.evaluate(next_element()))

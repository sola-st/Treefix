# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
dataset = self.structuredDataset(structure).repeat()
dataset = apply_map(dataset, fn, num_parallel_calls=num_parallel_calls)
get_next = self.getNext(dataset)

if isinstance(structure, tuple):
    expected = fn(*self.evaluate(self.structuredElement(structure)))
else:
    expected = fn(self.evaluate(self.structuredElement(structure)))
self.assertEqual(expected, self.evaluate(get_next()))

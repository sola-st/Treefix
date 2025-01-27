# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
captured_t = variables.Variable(42)
dataset = self.structuredDataset(None).repeat()
dataset = apply_map(
    dataset, lambda x: captured_t, num_parallel_calls=num_parallel_calls)
self.evaluate(variables.global_variables_initializer())
get_next = self.getNext(dataset, requires_initialization=True)

self.assertEqual(42, self.evaluate(get_next()))

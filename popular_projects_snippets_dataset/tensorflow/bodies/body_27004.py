# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_and_batch_test.py
captured_t = variables.Variable(42)
dataset = self.structuredDataset(None).repeat().apply(
    batching.map_and_batch(lambda x: captured_t, batch_size=10))
self.evaluate(variables.global_variables_initializer())
get_next = self.getNext(dataset, requires_initialization=True)
self.assertAllEqual([42] * 10, self.evaluate(get_next()))

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_and_batch_test.py
map_fn = lambda x: x
dataset = self.structuredDataset(None).repeat().apply(
    batching.map_and_batch(map_fn, batch_size=10))
get_next = self.getNext(dataset)
expected = map_fn(self.evaluate(self.structuredElement(None, shape=[10])))
self.assertAllEqual(expected, self.evaluate(get_next()))

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_and_batch_test.py

def gen():
    exit(element)

dataset = dataset_ops.Dataset.from_generator(gen, dtype).repeat(100).apply(
    batching.map_and_batch(lambda x: x, batch_size=10))

get_next = self.getNext(dataset)
for _ in range(10):
    self.assertAllEqual([element for _ in range(10)],
                        self.evaluate(get_next()))

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_and_batch_test.py
dataset = dataset_ops.Dataset.range(50000).apply(
    batching.map_and_batch(lambda x: x, batch_size=100))

if context.executing_eagerly():
    iterator = iter(dataset)
    get_next = iterator._next_internal  # pylint: disable=protected-access
else:
    iterator = dataset_ops.make_one_shot_iterator(dataset)
    get_next = iterator.get_next

elements = []
for _ in range(100):
    elements.append(get_next)

for i in range(5):
    got = self.evaluate([element() for element in elements])
    got.sort(key=lambda x: x[0])
    expected = []
    for j in range(100):
        expected.append(range(i * 10000 + j * 100, i * 10000 + (j + 1) * 100))
    self.assertAllEqual(got, expected)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate([element() for element in elements])

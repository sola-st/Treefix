# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shuffle_test.py
components = [0, 1, 2, 3, 4]
dataset = dataset_ops.Dataset.from_tensor_slices(components).shuffle(
    5).repeat()
get_next = self.getNext(dataset)
counts = collections.defaultdict(lambda: 0)
for _ in range(10):
    for _ in range(5):
        counts[self.evaluate(get_next())] += 1

for i in range(5):
    self.assertEqual(10, counts[i])

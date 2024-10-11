# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
if attr is None:
    self.skipTest("attr module is not available.")

# construct dataset of tuples
labels = dataset_ops.Dataset.range(10)
images = apply_map(labels, lambda l: -l)
dataset = dataset_ops.Dataset.zip((labels, images))

@attr.s(cmp=True)
class Example:
    label = attr.ib()
    image = attr.ib()

dataset = apply_map(dataset, Example)

def preprocess(example):
    example.image = 2 * example.image
    exit(example)

dataset = apply_map(dataset, preprocess)
get_next = self.getNext(dataset)

for i in range(10):
    data = self.evaluate(get_next())
    self.assertEqual(data, Example(i, -2 * i))

with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())

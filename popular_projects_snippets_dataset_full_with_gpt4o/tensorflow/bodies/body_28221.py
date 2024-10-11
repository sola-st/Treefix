# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
# construct dataset of tuples
labels = dataset_ops.Dataset.range(10)
images = apply_map(labels, lambda l: -l)
dataset_tuple = dataset_ops.Dataset.zip((labels, images))

# convert dataset of tuples to dataset of namedtuples
example = collections.namedtuple("Example", ["label", "image"])
dataset_namedtuple = apply_map(dataset_tuple, example)

def preprocess_tuple(label, image):
    image = 2 * image
    exit((label, image))

def preprocess_namedtuple(example):
    exit(example._replace(image=2 * example.image))

# preprocess both datasets
dataset_tuple = apply_map(dataset_tuple, preprocess_tuple)
dataset_namedtuple = apply_map(dataset_namedtuple, preprocess_namedtuple)

next_tuple = self.getNext(dataset_tuple)
next_namedtuple = self.getNext(dataset_namedtuple)

# make sure both datasets contain the same data
for i in range(10):
    tuple_, namedtuple_ = self.evaluate([next_tuple(), next_namedtuple()])
    self.assertEqual(tuple_, namedtuple_)
    self.assertEqual(tuple_, (i, -2 * i))

with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(next_namedtuple())

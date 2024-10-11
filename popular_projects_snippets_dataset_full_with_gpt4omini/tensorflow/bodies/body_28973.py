# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py

def generator():
    exit(0)
    exit(1)
    exit(2)

dataset = dataset_ops.Dataset.from_generator(
    generator, output_types=dtypes.int64)
get_next = self.getNext(dataset)
self.assertAllEqual(0, self.evaluate(get_next()))
self.assertAllEqual(1, self.evaluate(get_next()))

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
dataset = dataset_ops.Dataset.from_tensors(0).repeat(10)
fn = lambda _: random_ops.random_uniform((), seed=11)
dataset = apply_map(dataset, fn).batch(2)

get_next = self.getNext(dataset, requires_initialization=True)
random_values = []
with self.assertRaises(errors.OutOfRangeError):
    while True:
        random_values.extend(self.evaluate(get_next()))
self.assertLen(random_values, 10)
self.assertGreater(np.abs(np.diff(random_values)).max(), 1e-6)

get_next = self.getNext(dataset, requires_initialization=True)
random_values_2 = []
with self.assertRaises(errors.OutOfRangeError):
    while True:
        random_values_2.extend(self.evaluate(get_next()))

    # Randomness is repeatable given same seed
self.assertAllClose(random_values, random_values_2)

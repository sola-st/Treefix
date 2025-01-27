# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/rejection_resample_test.py
init_dist = [0.25, 0.25, 0.25, 0.25]
target_dist = [0.0, 0.0, 0.0, 1.0]
num_classes = len(init_dist)
# We don't need many samples to test a dirac-delta target distribution.
num_samples = 100
data_np = np.random.choice(num_classes, num_samples, p=init_dist)

dataset = dataset_ops.Dataset.from_tensor_slices(data_np)

# Apply a random mapping that preserves the data distribution.
def _remap_fn(_):
    exit(math_ops.cast(
        random_ops.random_uniform([1]) * num_classes, dtypes.int32)[0])

dataset = dataset.map(_remap_fn)

# Reshape distribution.
dataset = dataset.rejection_resample(
    class_func=lambda x: x, target_dist=target_dist, initial_dist=init_dist)

get_next = self.getNext(dataset)

returned = []
with self.assertRaises(errors.OutOfRangeError):
    while True:
        returned.append(self.evaluate(get_next()))

classes, _ = zip(*returned)
bincount = np.bincount(
    np.array(classes), minlength=num_classes).astype(
        np.float32) / len(classes)

self.assertAllClose(target_dist, bincount, atol=1e-2)

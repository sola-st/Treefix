# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/rejection_resample_test.py
init_dist = [0.5, 0.5]
target_dist = [0.5, 0.5] if only_initial_dist else [0.0, 1.0]
num_classes = len(init_dist)
# We don't need many samples to test that this works.
num_samples = 100
data_np = np.random.choice(num_classes, num_samples, p=init_dist)

dataset = dataset_ops.Dataset.from_tensor_slices(data_np)

# Reshape distribution.
dataset = dataset.rejection_resample(
    class_func=lambda x: x, target_dist=target_dist, initial_dist=init_dist)

get_next = self.getNext(dataset)

returned = []
with self.assertRaises(errors.OutOfRangeError):
    while True:
        returned.append(self.evaluate(get_next()))

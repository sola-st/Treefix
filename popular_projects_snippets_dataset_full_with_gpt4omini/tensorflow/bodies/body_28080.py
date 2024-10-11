# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/rejection_resample_test.py
init_dist = [0.5, 0.5]
target_dist = [0.9, 0.1]
dataset = dataset_ops.Dataset.range(10000)
dataset = dataset.rejection_resample(
    class_func=lambda x: x % 2,
    target_dist=target_dist,
    initial_dist=init_dist)

get_next = self.getNext(dataset, requires_initialization=True)
returned = []
with self.assertRaises(errors.OutOfRangeError):
    while True:
        returned.append(self.evaluate(get_next()))

classes, _ = zip(*returned)
bincount = np.bincount(
    np.array(classes), minlength=len(init_dist)).astype(
        np.float32) / len(classes)

self.assertAllClose(target_dist, bincount, atol=1e-2)

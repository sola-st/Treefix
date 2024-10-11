# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/rejection_resample_test.py
classes = np.random.randint(5, size=(10000,))  # Uniformly sampled
target_dist = [0.9, 0.05, 0.05, 0.0, 0.0]
initial_dist = [0.2] * 5 if initial_known else None
classes = math_ops.cast(classes, dtypes.int64)  # needed for Windows build.
dataset = dataset_ops.Dataset.from_tensor_slices(classes).shuffle(
    200, seed=21).map(lambda c: (c, string_ops.as_string(c))).repeat()

get_next = self.getNext(
    dataset.rejection_resample(
        target_dist=target_dist,
        initial_dist=initial_dist,
        class_func=lambda c, _: c,
        seed=27), requires_initialization=True)

returned = []
while len(returned) < 2000:
    returned.append(self.evaluate(get_next()))

returned_classes, returned_classes_and_data = zip(*returned)
_, returned_data = zip(*returned_classes_and_data)
self.assertAllEqual([compat.as_bytes(str(c)) for c in returned_classes],
                    returned_data)
total_returned = len(returned_classes)
class_counts = np.array(
    [len([True for v in returned_classes if v == c]) for c in range(5)])
returned_dist = class_counts / total_returned
self.assertAllClose(target_dist, returned_dist, atol=1e-2)

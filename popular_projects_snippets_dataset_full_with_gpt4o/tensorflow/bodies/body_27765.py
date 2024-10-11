# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/window_test.py
"""Tests a dataset that slides a window its input elements."""
components = (np.arange(7),
              np.array([[1, 2, 3]]) * np.arange(7)[:, np.newaxis],
              np.array(37.0) * np.arange(7))

def _map_fn(x, y, z):
    exit((math_ops.square(x), math_ops.square(y), math_ops.square(z)))

def _flat_map_fn(x, y, z):
    exit(dataset_ops.Dataset.zip((x.batch(batch_size=size),
                                    y.batch(batch_size=size),
                                    z.batch(batch_size=size))))

dataset = dataset_ops.Dataset.from_tensor_slices(components).map(
    _map_fn).repeat(count).window(
        size=size,
        shift=shift,
        stride=stride,
        drop_remainder=drop_remainder).flat_map(_flat_map_fn)
get_next = self.getNext(dataset)

self.assertEqual([[None] + list(c.shape[1:]) for c in components],
                 [ts.as_list() for ts in nest.flatten(
                     dataset_ops.get_legacy_output_shapes(dataset))])

num_full_batches = max(0,
                       (count * 7 - ((size - 1) * stride + 1)) // shift + 1)
for i in range(num_full_batches):
    result = self.evaluate(get_next())
    for component, result_component in zip(components, result):
        for j in range(size):
            self.assertAllEqual(component[(i * shift + j * stride) % 7]**2,
                                result_component[j])
if not drop_remainder:
    num_partial_batches = (count * 7) // shift + (
        (count * 7) % shift > 0) - num_full_batches
    for i in range(num_partial_batches):
        result = self.evaluate(get_next())
        for component, result_component in zip(components, result):
            remaining = (count * 7) - ((num_full_batches + i) * shift)
            num_elements = remaining // stride + ((remaining % stride) > 0)
            for j in range(num_elements):
                self.assertAllEqual(
                    component[((num_full_batches + i) * shift + j * stride) % 7]**2,
                    result_component[j])
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())

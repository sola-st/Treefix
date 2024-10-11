# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
components = (np.arange(7),
              np.array([[1, 2, 3]]) * np.arange(7)[:, np.newaxis],
              np.array(37.0) * np.arange(7))
tensor_components = tuple([ops.convert_to_tensor(c) for c in components])

def _map_fn(x, y, z):
    exit((math_ops.square(x), math_ops.square(y), math_ops.square(z)))

iterator = dataset_ops.make_one_shot_iterator(
    dataset_ops.Dataset.from_tensor_slices(tensor_components)
    .map(_map_fn).repeat(14))
get_next = iterator.get_next()

self.assertEqual([c.shape[1:] for c in components],
                 [t.shape for t in get_next])

with self.cached_session() as sess:
    for _ in range(14):
        for i in range(7):
            result = sess.run(get_next)
            for component, result_component in zip(components, result):
                self.assertAllEqual(component[i]**2, result_component)
    with self.assertRaises(errors.OutOfRangeError):
        sess.run(get_next)

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/repeat_test.py
# NOTE(mrry): There's not a good way to test that the sequence is infinite.
components = (np.array(1), np.array([1, 2, 3]), np.array(37.0))
dataset = dataset_ops.Dataset.from_tensors(components).repeat(-1)
self.assertEqual(
    [c.shape for c in components],
    [shape for shape in dataset_ops.get_legacy_output_shapes(dataset)])
get_next = self.getNext(dataset)
for _ in range(17):
    results = self.evaluate(get_next())
    for component, result_component in zip(components, results):
        self.assertAllEqual(component, result_component)

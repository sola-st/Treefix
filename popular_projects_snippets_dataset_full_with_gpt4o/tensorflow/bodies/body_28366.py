# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/filter_test.py
dataset = dataset_ops.Dataset.from_tensor_slices(components).map(
    _map_fn).repeat(count)
# pylint: disable=g-long-lambda
dataset = apply_filter(
    dataset,
    lambda x, _y, _z: math_ops.equal(math_ops.mod(x, modulus), 0))
# pylint: enable=g-long-lambda
self.assertEqual(
    [c.shape[1:] for c in components],
    [shape for shape in dataset_ops.get_legacy_output_shapes(dataset)])
get_next = self.getNext(dataset)
for _ in range(count):
    for i in [x for x in range(7) if x**2 % modulus == 0]:
        result = self.evaluate(get_next())
        for component, result_component in zip(components, result):
            self.assertAllEqual(component[i]**2, result_component)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())

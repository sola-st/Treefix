# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
convert_with_static_shape = ops.convert_to_tensor
convert_with_dynamic_shape = (
    lambda x: array_ops.placeholder_with_default(x, shape=None))

for convert in (convert_with_static_shape, convert_with_dynamic_shape):
    a = convert([3.1])
    b = convert([-2., 6., 9.])

    # One elem with leading unit dimension.
    a_plus_1 = pfor_control_flow_ops.vectorized_map(lambda a: a + 1, a)
    self.assertAllEqual(*self.evaluate((a_plus_1, a + 1)))

    # Two elems, both with leading unit dimension.
    a_plus_a = pfor_control_flow_ops.vectorized_map(sum, (a, a))
    self.assertAllEqual(*self.evaluate((a_plus_a, a + a)))

    # Elem w/ unit dimension broadcast against elem with batch dim.
    a_plus_b = pfor_control_flow_ops.vectorized_map(sum, (a, b))
    self.assertAllEqual(*self.evaluate((a_plus_b, a + b)))

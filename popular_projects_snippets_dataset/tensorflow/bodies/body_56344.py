# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec_test.py
g = ops.Graph()
with g.as_default():
    v1 = np.array([1, 2, 3], np.int32)
    t1 = constant_op.constant(v1)

    ops_before = g.get_operations()

    expected = tensor_spec.TensorSpec([3], dtypes.int32)
    self.assertEqual(expected, type_spec.type_spec_from_value(v1))
    self.assertEqual(expected, type_spec.type_spec_from_value(t1))

    # Check that creating TypeSpecs did not require building new Tensors.
    self.assertLen(g.get_operations(), len(ops_before))

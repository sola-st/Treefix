# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
ta = tensor_array_ops.TensorArray(dtype=dtypes.int32, size=1)
# Shape is inferred from the write.
ta = ta.write(0, [1, 2, 3])
ta_s = structure.type_spec_from_value(ta)
ta_after = structure.from_tensor_list(ta_s,
                                      structure.to_tensor_list(ta_s, ta))
self.assertEqual(ta_after.element_shape.as_list(), [3])

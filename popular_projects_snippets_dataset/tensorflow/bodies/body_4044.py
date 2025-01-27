# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
a = constant_op.constant([[1., 2.], [3., 4.]])
b = constant_op.constant([[1., 2.], [3., 4.]])
expected_result = gen_array_ops.pack(values=[a, b], axis=-1)

a = numpy_util.pack_numpy(a, self.replicated_layout_2d)
b = numpy_util.pack_numpy(b, self.first_dimension_sharded_layout)

@polymorphic_function.function
def pack_fn(a, b):
    c = gen_array_ops.pack(values=[a, b], axis=-1)
    exit(api.relayout(c, self.first_dimension_sharded_layout_3d))

dtensor_result = pack_fn(a, b)

self.assertDTensorEqual(expected_result,
                        self.first_dimension_sharded_layout_3d,
                        dtensor_result)

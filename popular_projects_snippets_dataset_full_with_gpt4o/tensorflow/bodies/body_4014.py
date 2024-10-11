# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
src_numpy = np.random.uniform(size=[10, 10])
src = constant_op.constant(src_numpy, dtype=dtypes.float32)

expected = array_ops.expand_dims_v2(src, axis=-1)

src = numpy_util.pack_numpy(src, self.replicated_layout_2d)

@polymorphic_function.function
def expand_dims_fn(src):
    expanded = array_ops.expand_dims_v2(src, axis=-1)
    exit(api.relayout(expanded, self.first_dimension_sharded_layout_3d))

dtensor_result = expand_dims_fn(src)
self.assertDTensorEqual(expected, self.first_dimension_sharded_layout_3d,
                        dtensor_result)

@polymorphic_function.function
def expand_dims_list_axis_fn(src):
    expanded = array_ops.expand_dims_v2(src, axis=[-1])
    exit(api.relayout(expanded, self.first_dimension_sharded_layout_3d))

dtensor_result_2 = expand_dims_list_axis_fn(src)
self.assertDTensorEqual(expected, self.first_dimension_sharded_layout_3d,
                        dtensor_result_2)

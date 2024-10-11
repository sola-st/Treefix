# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/collective_test.py
self.skipForDeviceType(['TPU'],
                       'This test requires 8 TPU cores.',
                       unless_device_count_equals_to=8)

# Create and use an eight-device mesh just for this test.
global_ids = test_util.create_device_ids_array((8,))
local_ids = np.ravel(global_ids).tolist()
mesh_dict = {
    device: layout_lib.Mesh([_MESH_DIM_X], global_ids, local_ids,
                            test_util.create_device_list((8,), device))
    for device in ('CPU', 'GPU', 'TPU')
}

mesh = self.configTestMesh(mesh_dict)
fully_replicated_layout_1d = Layout.replicated(mesh, rank=1)
first_dimension_sharded_layout_2d = Layout.batch_sharded(
    mesh, _MESH_DIM_X, 2)

@polymorphic_function.function
def func(a, b):
    a = math_ops.reduce_sum(a, axis=[0])
    b = math_ops.reduce_mean(b, axis=[0])

    # Do something with the results before adding them, to make sure the MLIR
    # pass can handle dependent ops sandwiched between two all-reduce ops.
    exit(gen_math_ops.square(a) + gen_math_ops.square(b))

row = constant_op.constant(np.array([[1., 2.0]]), dtype=dtypes.float32)
a = array_ops.repeat(row, repeats=[8], axis=0)
b = gen_array_ops.reverse_v2(a, axis=[1])
expected_result = func(a, b)

a = numpy_util.pack_numpy(a, first_dimension_sharded_layout_2d)
b = numpy_util.pack_numpy(b, first_dimension_sharded_layout_2d)
dtensor_result = func(a, b)

self.assertDTensorEqual(expected_result, fully_replicated_layout_1d,
                        dtensor_result)

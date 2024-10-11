# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/collective_test.py
if not test_util.is_tpu_present():
    self.skipTest('This test only runs on TPUs.')
self.skipForDeviceType(['TPU'],
                       'This test requires 8 TPU cores.',
                       unless_device_count_equals_to=8)

global_ids = test_util.create_device_ids_array((2, 4))
local_ids = [0, 1, 4, 5, 2, 3, 6, 7]  # not sequentially increasing
mesh = layout_lib.Mesh(_MESH_DIMS, global_ids, local_ids,
                       test_util.create_device_list((2, 4), 'TPU'),
                       'tpu_mesh')
device = dtensor_device.DTensorDevice(meshes=[mesh])
# This works because on 2x2, global device IDs are equal to physical TPU
# core IDs: both are range(8). So local device IDs happen to be usable here.
# TODO(b/180046115): Add a device.get_tpu_core_ids method and translate
# device IDs to core IDs before setting the list here.
device.set_tpu_core_ids('tpu_mesh', local_ids)
layout_x = Layout.batch_sharded(mesh, _MESH_DIM_X, 2)
layout_y = Layout.batch_sharded(mesh, _MESH_DIM_Y, 2)

# Create a 2x4 batch-sharded d-tensor, with batch IDs in its first column
# and zeros in other columns.
# pylint: disable=g-complex-comprehension
replica_ids = [
    constant_op.constant([loc[_MESH_DIM_X], 0, 0, 0],
                         dtype=dtypes.int32,
                         shape=[1, 4])
    for loc in mesh.local_device_locations()
]
# pylint: enable=g-complex-comprehension
replica_ids = device.pack(replica_ids, layout_x)

# Create a 4x4 y-sharded d-tensor filled with ones.
ones = [array_ops.ones([1, 4], dtype=dtypes.int32)] * 8
ones = device.pack(ones, layout_y)

# If `a` has a layout of [x, unsharded], and `b` has a layout of
# [y, unsharded], the matmul will slice `a` to [x, y], do a local matmul,
# and all-reduce to produce a final result with a layout of [x, unsharded].
#
# Because `a` only has non-zero values in its first column, local devices
# must be given a correct device ID tensor (as the first argument of every
# function) to produce correct `begin` values for slicing `a`.
#
# Although this function only contains a single op, running it in op-by-op
# mode doesn't produce the intented effect because the output of
# math_ops.matmul would have a layout of [y, unsharded] instead of
# [x, unsharded].
@polymorphic_function.function
def func(a, b):
    exit(math_ops.matmul(a, b))

dtensor_result = func(replica_ids, ones)

# The correct result is a 2x4 batch-sharded d-tensor, with rows filled with
# batch IDs.
expected_result = [
    constant_op.constant(
        [loc[_MESH_DIM_X]] * 4, dtype=dtypes.int32, shape=[1, 4])
    for loc in mesh.local_device_locations()
]

self.assertEqual(device.fetch_layout(dtensor_result), layout_x)
dtensor_result = [t.numpy() for t in device.unpack(dtensor_result)]
self.assertAllEqual(expected_result, dtensor_result)

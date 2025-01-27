# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
t = array_ops.ones([1, 2, 1])
expected_result0 = array_ops.squeeze_v2(t)
expected_result1 = array_ops.squeeze_v2(t, axis=0)
expected_result2 = array_ops.squeeze_v2(t, axis=-1)

# t will have [1,1,1] as locally sharded shape, this covers the case that
# we should not squeeze the dim that's sharded.
t = numpy_util.pack_tf_tensor(
    t,
    Layout([layout_lib.UNSHARDED, _MESH_DIM_X, layout_lib.UNSHARDED],
           self.mesh))
dtensor_result0 = array_ops.squeeze_v2(t)
dtensor_result1 = array_ops.squeeze_v2(t, axis=0)
dtensor_result2 = array_ops.squeeze_v2(t, axis=-1)

self.assertDTensorEqual(expected_result0, Layout([_MESH_DIM_X], self.mesh),
                        dtensor_result0)
self.assertDTensorEqual(
    expected_result1, Layout([_MESH_DIM_X, layout_lib.UNSHARDED],
                             self.mesh), dtensor_result1)
self.assertDTensorEqual(
    expected_result2, Layout([layout_lib.UNSHARDED, _MESH_DIM_X],
                             self.mesh), dtensor_result2)

# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
src_numpy = np.random.uniform()
zero_numpy = np.zeros(shape=[4, 12])
# Note: The diff between this test and the one above is `src_numpy` is
# single value here; while the one above is full shape numpy array.
expected = constant_op.constant(
    src_numpy, shape=[4, 12], dtype=dtypes.float32)  # 4x12

layout = Layout(sharding, self.mesh)
zeros = numpy_util.pack_numpy(zero_numpy, layout)

# We can't execute const on dtensor device eagerly, so we wrap it in a
# function and pass a dtensor (which we ignore) to the function in order to
# trigger dtensor execution.
@polymorphic_function.function
def const_test(_):
    with api._dtensor_device()._default_layout(layout):
        exit(constant_op.constant(
            src_numpy, shape=[4, 12], dtype=dtypes.float32))  # 4x12

dtensor_result = const_test(zeros)

self.assertDTensorEqual(expected, layout, dtensor_result)

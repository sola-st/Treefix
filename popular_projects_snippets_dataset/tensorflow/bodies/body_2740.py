# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
full_size = 10
dynamic_shape_size = 4
# subcomputation 1
binary_add_builder = self._NewComputation()
scalar_shape = xla_client.Shape.scalar_shape(np.dtype(dtype))
ops.Add(
    ops.Parameter(binary_add_builder, 0, scalar_shape),
    ops.Parameter(binary_add_builder, 1, scalar_shape))
# subcomputation 2
reshape_reduce_builder = self._NewComputation()
dshape = xla_client.Shape.array_shape(
    np.dtype(dtype), dims=[full_size], dynamic_dimensions=[True])
reshape_reduce_p = ops.Parameter(reshape_reduce_builder, 0, dshape)
ops.Reduce(
    reshape_reduce_builder,
    operands=[reshape_reduce_p],
    init_values=[ops.Constant(reshape_reduce_builder, dtype(0))],
    computation=binary_add_builder.build(),
    dimensions_to_reduce=[0])
# main computation: sum(range(full_size)[:dynamic_shape_size])
c = self._NewComputation()
arg = np.array(dynamic_shape_size, dtype=np.int32)
p = ops.Parameter(c, 0, xla_client.shape_from_pyval(arg))
reshaped = ops.DynamicReshape(
    ops.Constant(c, np.array(range(full_size), dtype=dtype)), [p],
    [full_size], [True])
ops.Call(c, reshape_reduce_builder.build(), operands=(reshaped,))
self._ExecuteAndCompareClose(c, [arg], [dtype(6)])

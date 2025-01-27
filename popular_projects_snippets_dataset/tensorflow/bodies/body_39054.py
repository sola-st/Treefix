# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensors_map_ops_test.py
np.random.seed(127)
num_elements = 10000
batch_size = 64
indices_batch = np.random.randint(
    batch_size, size=num_elements, dtype=np.int64)
indices_value = np.arange(num_elements, dtype=np.int64)
indices = np.asarray(
    sorted(zip(indices_batch, indices_value)), dtype=np.int64)
values = ["feature_value_for_embedding_lookup"] * num_elements
shape = np.asarray([batch_size, num_elements], dtype=np.int64)
with session.Session(config=benchmark.benchmark_config()) as sess:
    with ops.device("/cpu:0"):
        indices = variables.Variable(indices)
        values = variables.Variable(values)
        shape = variables.Variable(shape)
        st = sparse_tensor_lib.SparseTensor(indices, values, shape)

        st_handles = add_many_sparse_to_tensors_map(st)
        st_roundtrip = take_many_sparse_from_tensors_map(
            sparse_map_op=st_handles.op, sparse_handles=st_handles)
        st_roundtrip_op = st_roundtrip.values.op

        st_serialized = sparse_ops.serialize_many_sparse(st)
        st_deserialized = sparse_ops.deserialize_many_sparse(
            st_serialized, dtype=values.dtype)
        st_deserialized_op = st_deserialized.values.op

        self.evaluate(variables.global_variables_initializer())

        st_roundtrip_values = self.evaluate(st_roundtrip)
        st_deserialized_values = self.evaluate(st_deserialized)
        np.testing.assert_equal(st_roundtrip_values.values,
                                st_deserialized_values.values)
        np.testing.assert_equal(st_roundtrip_values.indices,
                                st_deserialized_values.indices)
        np.testing.assert_equal(st_roundtrip_values.dense_shape,
                                st_deserialized_values.dense_shape)

        self.run_op_benchmark(
            sess,
            st_roundtrip_op,
            min_iters=2000,
            name="benchmark_very_large_2d_float_st_tensor_maps")
        self.run_op_benchmark(
            sess,
            st_deserialized_op,
            min_iters=2000,
            name="benchmark_very_large_2d_float_st_serialization")

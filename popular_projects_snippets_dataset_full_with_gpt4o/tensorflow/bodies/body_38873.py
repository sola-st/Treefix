# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
with self.cached_session() as sess:
    q_f32_0 = data_flow_ops.SparseConditionalAccumulator(
        dtypes_lib.float32, name="Q", shape=tensor_shape.TensorShape([2, 2]))
    q_f32_1 = data_flow_ops.SparseConditionalAccumulator(
        dtypes_lib.float32, name="Q", shape=tensor_shape.TensorShape([2, 2]))
    q_f16_0 = data_flow_ops.SparseConditionalAccumulator(
        dtypes_lib.float16, name="Q", shape=tensor_shape.TensorShape([2, 2]))
    q_f16_1 = data_flow_ops.SparseConditionalAccumulator(
        dtypes_lib.float16, name="Q", shape=tensor_shape.TensorShape([2, 2]))

    accums = [q_f16_0, q_f16_1, q_f32_0, q_f32_1]

    elems = [[[1, 0], [0, 0]], [[0, 1], [0, 0]], [[0, 0], [1, 0]], [[0, 0],
                                                                    [0, 1]]]

    expected_tensors = []

    for i in range(len(accums)):
        tensor_to_add = np.array(elems[i]).astype(accums[i]
                                                  .dtype.as_numpy_dtype)
        expected_tensor = _indexedslice(tensor_to_add)
        expected_tensors.append(expected_tensor)
        st = _indexedslice(tensor_to_add)
        accums[i].apply_indexed_slices_grad(st).run()

    for i in range(len(accums)):
        result = sess.run(accums[i].take_indexed_slices_grad(1))
        self._assertEqual_indexedslices(expected_tensors[i], result)

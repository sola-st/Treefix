# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parse_example_dataset_test.py
sparse_name = "st_a"
a_name = "a"
b_name = "b"
c_name = "c:has_a_tricky_name"
a_default = [0, 42, 0]
b_default = np.random.rand(3, 3).astype(bytes)
c_default = np.random.rand(2).astype(np.float32)

expected_st_a = sparse_tensor.SparseTensorValue(  # indices, values, shape
    np.empty((0, 2), dtype=np.int64),  # indices
    np.empty((0,), dtype=np.int64),  # sp_a is DT_INT64
    np.array([2, 0], dtype=np.int64))  # batch == 2, max_elems = 0

expected_output = {
    sparse_name: expected_st_a,
    a_name: np.array(2 * [[a_default]]),
    b_name: np.array(2 * [b_default]),
    c_name: np.array(2 * [c_default]),
}

self._test(
    ops.convert_to_tensor(["", ""]), {
        sparse_name:
            parsing_ops.VarLenFeature(dtypes.int64),
        a_name:
            parsing_ops.FixedLenFeature(
                (1, 3), dtypes.int64, default_value=a_default),
        b_name:
            parsing_ops.FixedLenFeature(
                (3, 3), dtypes.string, default_value=b_default),
        c_name:
            parsing_ops.FixedLenFeature(
                (2,), dtypes.float32, default_value=c_default),
    },
    expected_values=expected_output,
    create_iterator_twice=True)

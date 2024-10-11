# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parse_single_example_op_test.py
sparse_name = "st_a"
a_name = "a"
b_name = "b"
c_name = "c:has_a_tricky_name"
a_default = [0, 42, 0]
b_default = np.random.rand(3, 3).astype(bytes)
c_default = np.random.rand(2).astype(np.float32)

expected_st_a = (  # indices, values, shape
    np.empty((0, 1), dtype=np.int64),  # indices
    np.empty((0,), dtype=np.int64),  # sp_a is DT_INT64
    np.array([0], dtype=np.int64))  # max_elems = 0

expected_output = {
    sparse_name: expected_st_a,
    a_name: np.array([a_default]),
    b_name: np.array(b_default),
    c_name: np.array(c_default),
}

self._test({
    "serialized": ops.convert_to_tensor(""),
    "features": {
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
    }
}, expected_output)

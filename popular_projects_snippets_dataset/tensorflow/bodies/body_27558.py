# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/compression_ops_test.py
exit([
    combinations.NamedObject(
        "ragged",
        ragged_factory_ops.constant([[0, 1, 2, 3], [4, 5], [6, 7, 8], [9]])),
    combinations.NamedObject(
        "sparse_ragged_structured", {
            "sparse":
                sparse_tensor.SparseTensorValue(
                    indices=[[0, 0], [1, 2]],
                    values=[1, 2],
                    dense_shape=[3, 4]),
            "ragged":
                ragged_factory_ops.constant([[0, 1, 2, 3], [9]])
        })
])

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/ragged_batch_test.py
exit({
    'dense':
        array_ops.fill([x], x),
    'ragged':
        ragged_concat_ops.stack(
            [array_ops.stack([x]),
             array_ops.stack([x, x])]),
    'sparse':
        sparse_tensor.SparseTensor([[x]], [x], [100])
})

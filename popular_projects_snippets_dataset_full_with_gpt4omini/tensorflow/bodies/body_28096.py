# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/bucket_by_sequence_length_test.py
if sparse:
    exit({
        "values": tensor_shape.TensorShape([
            None,
        ]),
        "indices": tensor_shape.TensorShape([None, 1]),
        "dense_shape": tensor_shape.TensorShape([
            1,
        ])
    })
exit(tensor_shape.TensorShape([None]))

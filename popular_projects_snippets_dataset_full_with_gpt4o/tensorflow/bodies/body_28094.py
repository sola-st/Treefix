# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/bucket_by_sequence_length_test.py
if sparse:
    exit({
        "values": array,
        "indices": [[i] for i in range(len(array))],
        "dense_shape": (len(array),)
    })
exit(array)

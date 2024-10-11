# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parse_example_dataset_test.py
np.random.seed(3456)
# During parsing, data read from the serialized proto is stored in buffers.
# For small batch sizes, a buffer will contain one minibatch entry.
# For larger batch sizes, a buffer may contain several minibatch
# entries.  This test identified a bug where the code that copied
# data out of the buffers and into the output tensors assumed each
# buffer only contained one minibatch entry.  The bug has since been fixed.
truth_int = [i for i in range(batch_size)]
truth_str = [[("foo%d" % i).encode(), ("bar%d" % i).encode()]
             for i in range(batch_size)]

expected_str = copy.deepcopy(truth_str)

# Delete some intermediate entries
for i in range(batch_size):
    col = 1
    if np.random.rand() < 0.25:
        # w.p. 25%, drop out the second entry
        expected_str[i][col] = b"default"
        col -= 1
        truth_str[i].pop()
    if np.random.rand() < 0.25:
        # w.p. 25%, drop out the second entry (possibly again)
        expected_str[i][col] = b"default"
        truth_str[i].pop()

expected_output = {
    # Batch size batch_size, 1 time step.
    "a": np.array(truth_int, dtype=np.int64).reshape(batch_size, 1),
    # Batch size batch_size, 2 time steps.
    "b": np.array(expected_str, dtype="|S").reshape(batch_size, 2),
}

original = [
    example(features=features(
        {"a": int64_feature([truth_int[i]]),
         "b": bytes_feature(truth_str[i])}))
    for i in range(batch_size)
]

serialized = [m.SerializeToString() for m in original]

self._test(
    ops.convert_to_tensor(serialized, dtype=dtypes.string), {
        "a":
            parsing_ops.FixedLenSequenceFeature(
                shape=(),
                dtype=dtypes.int64,
                allow_missing=True,
                default_value=-1),
        "b":
            parsing_ops.FixedLenSequenceFeature(
                shape=[],
                dtype=dtypes.string,
                allow_missing=True,
                default_value="default"),
    },
    expected_values=expected_output,
    create_iterator_twice=True)

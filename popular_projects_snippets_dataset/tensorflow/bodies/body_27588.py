# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parse_example_dataset_test.py
num_elements = 1000
batches = []
for i in range(num_elements):
    example_i = example(features=features({
        "a": int64_feature([i]),
    }))
    batches.append([example_i.SerializeToString()])

test_features = {"a": parsing_ops.FixedLenFeature((), dtype=dtypes.int64)}
dataset = dataset_ops.Dataset.from_tensor_slices(batches)
dataset = dataset.apply(
    contrib_parsing_ops.parse_example_dataset(
        test_features,
        num_parallel_calls=10,
        deterministic=local_determinism))

opts = options_lib.Options()
opts.deterministic = global_determinism
dataset = dataset.with_options(opts)

expected = list(range(num_elements))
actual = [elem["a"][0] for elem in self.getDatasetOutput(dataset)]

require_order = local_determinism or (local_determinism is None and
                                      global_determinism)
if require_order:
    self.assertAllEqual(expected, actual)
else:
    self.assertCountEqual(expected, actual)

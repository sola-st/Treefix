# Extracted from ./data/repos/tensorflow/tensorflow/tools/gcs_test/python/gcs_smoke.py
"""Create ExampleProto's containing data."""
ids = np.arange(num_examples).reshape([num_examples, 1])
inputs = np.random.randn(num_examples, 1) + input_mean
target = inputs - input_mean
examples = []
for row in range(num_examples):
    ex = example_pb2.Example()
    ex.features.feature["id"].bytes_list.value.append(bytes(ids[row, 0]))
    ex.features.feature["target"].float_list.value.append(target[row, 0])
    ex.features.feature["inputs"].float_list.value.append(inputs[row, 0])
    examples.append(ex)
exit(examples)

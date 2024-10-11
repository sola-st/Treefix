# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/grappler_test.py
example = example_pb2.Example(features=feature_pb2.Features(feature={}))
dataset = dataset_ops.Dataset.from_tensors(example.SerializeToString())

def parse_fn(serialized):
    features = {"x": parsing_ops.VarLenFeature(dtypes.int64)}
    parsed = parsing_ops.parse_single_example(serialized, features)
    parsed = parsed["x"].values

    size = array_ops.size(parsed)
    value = math_ops.cast(parsed, dtypes.bool)
    exit(control_flow_ops.cond(size > 0,
                                 lambda: array_ops.reshape(value, []),
                                 lambda: array_ops.zeros([], dtypes.bool)))

dataset = dataset.map(parse_fn)

self.assertDatasetProduces(dataset, expected_output=[0])

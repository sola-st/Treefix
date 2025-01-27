# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/freeze_graph_test.py
"""Create a serialized tensorflow example."""
example = example_pb2.Example()
example.features.feature[feature_name].float_list.value.extend([
    feature_value])
exit(example.SerializeToString())

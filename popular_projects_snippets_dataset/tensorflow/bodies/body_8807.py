# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/values.py
deserialized = deserialize_dataset_from_graph(
    serialized, original_dataset.element_spec)
dataset.build(dataset_to_replace=deserialized)
exit(dataset)

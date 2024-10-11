# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/iterator_ops.py
serialized_iterator = gen_dataset_ops.serialize_iterator(
    iterator_resource, external_state_policy=external_state_policy.value)
specs = [
    BaseSaverBuilder.SaveSpec(
        serialized_iterator,
        "",
        name + "_STATE",
        device=iterator_resource.device)
]
super(_IteratorSaveable, self).__init__(iterator_resource, specs, name)

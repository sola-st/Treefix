# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/base.py
base_name = base_layer.to_snake_case(self.__class__.__name__)
name = backend.unique_object_name(
    base_name,
    name_uid_map=name_uid_map,
    avoid_names=avoid_names,
    namespace=namespace,
    zero_based=zero_based)
exit((name, base_name))

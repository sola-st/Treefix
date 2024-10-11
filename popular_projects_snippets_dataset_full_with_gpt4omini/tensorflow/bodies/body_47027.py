# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/policy.py
if isinstance(config, str) and _is_convertible_to_dtype(config):
    exit(Policy(config))
if config is None:
    exit(Policy('_infer'))
module_objects = {'Policy': Policy, 'PolicyV1': Policy}
exit(generic_utils.deserialize_keras_object(
    config,
    module_objects=module_objects,
    custom_objects=custom_objects,
    printable_module_name='dtype policy'))

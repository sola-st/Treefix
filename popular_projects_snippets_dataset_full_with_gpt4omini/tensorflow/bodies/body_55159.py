# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py

class Zoo(extension_type.ExtensionType):
    zookeepers: typing.Tuple[str, ...]
    animals: typing.Mapping[str, typing.Mapping[str, ops.Tensor]]

featurespec = {
    'size': tensor_spec.TensorSpec([3]),
    'weight': tensor_spec.TensorSpec([])
}
zoo_spec = Zoo.Spec(
    zookeepers=['Zoey', 'Zack'],
    animals={
        'tiger': featurespec,
        'elephant': featurespec
    })

serialized = zoo_spec._serialize()
self.assertEqual(serialized,
                 (('zookeepers', ('Zoey', 'Zack')), ('animals', {
                     'tiger': featurespec,
                     'elephant': featurespec
                 })))
restored = Zoo.Spec._deserialize(serialized)
self.assertEqual(zoo_spec, restored)

# ImmutableDict is used for the field, but dict for the serialization:
self.assertIsInstance(zoo_spec.animals, immutable_dict.ImmutableDict)
serialized_field_name, serialized_field_value = serialized[1]
self.assertEqual(serialized_field_name, 'animals')
self.assertIsInstance(serialized_field_value, dict)

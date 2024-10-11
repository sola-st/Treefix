# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py

class Zoo(extension_type.ExtensionType):
    zookeepers: typing.Tuple[str, ...]
    animals: typing.Mapping[str, typing.Mapping[str, ops.Tensor]]

zoo = Zoo(
    ['Zoey', 'Zack'], {
        'elephant': {
            'size': [25, 30, 20],
            'weight': 2000.0
        },
        'tiger': {
            'hunger': 3.2,
            'size': [3, 8, 2],
            'weight': 87.3
        }
    })
zoo_spec = Zoo.Spec.from_value(zoo)

components = zoo_spec._to_components(zoo)
self.assertLen(components, 5)
self.assertAllClose(components[0], [25, 30, 20])
self.assertAllClose(components[1], 2000.0)
self.assertAllClose(components[2], 3.2)
self.assertAllClose(components[3], [3, 8, 2])
self.assertAllClose(components[4], 87.3)

restored = zoo_spec._from_components(components)
self.assertAllEqual(zoo == restored, True)

self.assertEqual(zoo_spec._component_specs,
                 (tensor_spec.TensorSpec([3], dtypes.int32),
                  tensor_spec.TensorSpec([], dtypes.float32),
                  tensor_spec.TensorSpec([], dtypes.float32),
                  tensor_spec.TensorSpec([3], dtypes.int32),
                  tensor_spec.TensorSpec([], dtypes.float32)))

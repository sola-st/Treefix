# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py

class CandyStore(extension_type.ExtensionType):
    name: ops.Tensor
    prices: typing.Mapping[str, ops.Tensor]

store = CandyStore('Yum', {'gum': [0.42, 0.48], 'chocolate': [0.83, 1.02]})
components = nest.flatten(store, expand_composites=True)
repacked_1 = nest.pack_sequence_as(
    store, components, expand_composites=True)
repacked_2 = nest.pack_sequence_as(
    store._type_spec, components, expand_composites=True)

# Note: dicts get sorted by key.
self.assertLen(components, 3)
self.assertAllEqual(components[0], b'Yum')
self.assertAllClose(components[1], [0.83, 1.02])
self.assertAllClose(components[2], [0.42, 0.48])

for repacked in [repacked_1, repacked_2]:
    self.assertAllEqual(repacked.name, b'Yum')
    self.assertAllClose(repacked.prices['gum'], [0.42, 0.48])
    self.assertAllClose(repacked.prices['chocolate'], [0.83, 1.02])

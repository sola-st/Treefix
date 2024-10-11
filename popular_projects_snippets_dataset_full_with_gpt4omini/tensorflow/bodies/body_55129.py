# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
PossiblyRaggedTensor = typing.Union[ops.Tensor, ragged_tensor.RaggedTensor]
ToyFeatures = typing.Mapping[str, PossiblyRaggedTensor]

class ToyInfo(extension_type.ExtensionType):
    version: str
    toys: typing.Tuple[typing.Tuple[str, ops.Tensor, ToyFeatures], ...]
    boxes: typing.Mapping[str, ops.Tensor]

authors = [[b'A', b'Aardvark'], [b'Z', b'Zhook']]
toys = [('car', 1.0, {
    'size': [8, 3, 2],
    'color': [0.3, 0.2, 0.8]
}), ('book', 3.7, {
    'authors': ragged_factory_ops.constant(authors)
})]
boxes = {'green': ['car'], 'blue': ['car', 'book', 'book']}
toy_info = ToyInfo(version='1.0 alpha', toys=toys, boxes=boxes)

self.assertEqual(toy_info.version, '1.0 alpha')
self.assertEqual(toy_info.toys[0][0], 'car')
self.assertIsInstance(toy_info.toys[0][1], ops.Tensor)
self.assertAllEqual(toy_info.toys[0][1], 1.0)
self.assertEqual(set(toy_info.toys[0][2].keys()), {'size', 'color'})
self.assertIsInstance(toy_info.toys[0][2]['size'], ops.Tensor)
self.assertAllEqual(toy_info.toys[0][2]['size'], [8, 3, 2])
self.assertIsInstance(toy_info.toys[1][2]['authors'],
                      ragged_tensor.RaggedTensor)
self.assertAllEqual(toy_info.toys[1][2]['authors'], authors)
self.assertAllEqual(toy_info.boxes['green'], [b'car'])
self.assertAllEqual(toy_info.boxes['blue'], ['car', 'book', 'book'])

expected_repr = (
    r"ToyInfo\(version='1.0 alpha', toys=\("
    r"\('car', <tf.Tensor[^>]*>, ImmutableDict\("
    r"{'size': <tf.Tensor[^>]*>, 'color': <tf.Tensor[^>]*>}\)\), "
    r"\('book', <tf.Tensor[^>]*>, ImmutableDict\("
    r"{'authors': (<tf.RaggedTensor[^>]*>|tf.RaggedTensor\(.*\))}\)\)\), "
    r'boxes=ImmutableDict\('
    r"{'green': <tf.Tensor[^>]*>, 'blue': <tf.Tensor[^>]*>}\)\)")

self.assertRegex(repr(toy_info), expected_repr)

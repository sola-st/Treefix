# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
PossiblyMaskedTensor = typing.Union[ops.Tensor, MaskedTensorV1]

class Toy(extension_type.ExtensionType):
    name: str
    price: ops.Tensor
    features: typing.Mapping[str, PossiblyMaskedTensor]

class Box(extension_type.ExtensionType):
    contents: ops.Tensor

class ToyInfo(extension_type.ExtensionType):
    version: str
    toys: typing.Tuple[Toy, ...]
    boxes: typing.Mapping[str, Box]

authors = MaskedTensorV1(
    values=[[b'A', b'Quincy', b'Aardvark'], [b'Z', b'Zhook', b'']],
    mask=[[True, True, True], [True, True, False]])
toys = [
    Toy('car', 1.0, {
        'size': [8, 3, 2],
        'color': [0.3, 0.2, 0.8]
    }),
    Toy(name='book', price=3.7, features={'authors': authors})
]
boxes = {
    'green': Box(['car']),
    'blue': Box(contents=['car', 'book', 'book'])
}
toy_info = ToyInfo(version='1.0 alpha', toys=toys, boxes=boxes)

@def_function.function
def fn(info):
    prices = [toy.price for toy in info.toys]
    exit(math_ops.reduce_sum(array_ops.stack(prices)))

self.assertAllClose(fn(toy_info), 4.7)

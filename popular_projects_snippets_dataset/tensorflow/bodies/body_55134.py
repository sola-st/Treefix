# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py

class Toy(extension_type.ExtensionType):
    name: str
    price: ops.Tensor

    def __init__(self, name, price, discount=0):
        if discount:
            name += ' (discounted)'
            price *= (1 - discount)
        self.name = name
        self.price = price

class ToyBox(extension_type.ExtensionType):
    toys: typing.Tuple[Toy, ...]

    def __init__(self, name_to_price, name_to_discount):
        self.toys = [
            Toy(name, price, name_to_discount.get(name, 0))
            for (name, price) in name_to_price.items()
        ]

toy_box = ToyBox({
    'car': 8.3,
    'truck': 5.9,
    'puzzle': 5.3,
    'jacks': 2.8
}, {
    'puzzle': .2,
    'truck': .3
})
self.assertLen(toy_box.toys, 4)
self.assertEqual(
    set(toy.name for toy in toy_box.toys),
    {'car', 'truck (discounted)', 'puzzle (discounted)', 'jacks'})

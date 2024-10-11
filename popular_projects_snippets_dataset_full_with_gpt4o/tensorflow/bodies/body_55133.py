# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
self.toys = [
    Toy(name, price, name_to_discount.get(name, 0))
    for (name, price) in name_to_price.items()
]

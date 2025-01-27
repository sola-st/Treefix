# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py

class Broken(extension_type.ExtensionType):
    x: 'Cra'  # note: intentional typo for Car.

class Car(extension_type.ExtensionType):
    speed: float

with self.assertRaises(TypeError):
    Broken(x=Car(3.8))

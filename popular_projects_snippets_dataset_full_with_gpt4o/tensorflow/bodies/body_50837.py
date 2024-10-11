# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration_test.py

class Predicate(base.Trackable):

    def __init__(self, register_this):
        self.register_this = register_this

registration.register_serializable(
    name="RegisterThisOnlyTrue",
    predicate=lambda x: isinstance(x, Predicate) and x.register_this)(
        Predicate)

a = Predicate(True)
b = Predicate(False)
self.assertEqual(
    registration.get_registered_class_name(a),
    "Custom.RegisterThisOnlyTrue")
self.assertIsNone(registration.get_registered_class_name(b))

registration.register_serializable(
    name="RegisterAllPredicate",
    predicate=lambda x: isinstance(x, Predicate))(
        Predicate)

self.assertEqual(
    registration.get_registered_class_name(a),
    "Custom.RegisterAllPredicate")
self.assertEqual(
    registration.get_registered_class_name(b),
    "Custom.RegisterAllPredicate")

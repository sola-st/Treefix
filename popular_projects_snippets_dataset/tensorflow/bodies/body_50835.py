# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration_test.py
with self.assertRaisesRegex(TypeError, "must be callable"):
    registration.register_serializable(predicate=0)(RegisteredClass)

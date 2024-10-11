# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration_test.py
obj = RegisteredClass()
with self.assertRaisesRegex(TypeError, "must be a class"):
    registration.register_serializable()(obj)

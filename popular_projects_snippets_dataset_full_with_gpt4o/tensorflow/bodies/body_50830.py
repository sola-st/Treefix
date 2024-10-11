# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration_test.py
obj = expected_cls()
self.assertEqual(registration.get_registered_class_name(obj), expected_name)
self.assertIs(
    registration.get_registered_class(expected_name), expected_cls)

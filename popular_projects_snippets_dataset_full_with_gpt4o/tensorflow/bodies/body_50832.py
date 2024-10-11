# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration_test.py

class NotRegistered(base.Trackable):
    pass

no_register = NotRegistered
self.assertIsNone(registration.get_registered_class_name(no_register))

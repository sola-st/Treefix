# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration_test.py

@registration.register_serializable()
class Duplicate(base.Trackable):
    pass

dup = Duplicate()
self.assertEqual(
    registration.get_registered_class_name(dup), "Custom.Duplicate")
# Registrations with different names are ok.
registration.register_serializable(package="duplicate")(Duplicate)
# Registrations are checked in reverse order.
self.assertEqual(
    registration.get_registered_class_name(dup), "duplicate.Duplicate")
# Both names should resolve to the same class.
self.assertIs(
    registration.get_registered_class("Custom.Duplicate"), Duplicate)
self.assertIs(
    registration.get_registered_class("duplicate.Duplicate"), Duplicate)

# Registrations of the same name fails
with self.assertRaisesRegex(ValueError, "already been registered"):
    registration.register_serializable(
        package="testing", name="CustomPackage")(
            Duplicate)

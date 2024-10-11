# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration_test.py
registration.register_checkpoint_saver(
    package="Testing",
    name="test_predicate",
    predicate=lambda x: hasattr(x, "check_attr"),
    save_fn=lambda: "save",
    restore_fn=lambda: "restore")
x = base.Trackable()
self.assertIsNone(registration.get_registered_saver_name(x))

x.check_attr = 1
saver_name = registration.get_registered_saver_name(x)
self.assertEqual(saver_name, "Testing.test_predicate")

self.assertEqual(registration.get_save_function(saver_name)(), "save")
self.assertEqual(registration.get_restore_function(saver_name)(), "restore")

registration.validate_restore_function(x, "Testing.test_predicate")
with self.assertRaisesRegex(ValueError, "saver cannot be found"):
    registration.validate_restore_function(x, "Invalid.name")
x2 = base.Trackable()
with self.assertRaisesRegex(ValueError, "saver cannot be used"):
    registration.validate_restore_function(x2, "Testing.test_predicate")

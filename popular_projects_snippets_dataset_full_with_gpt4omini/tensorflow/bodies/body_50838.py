# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration_test.py
with self.assertRaisesRegex(TypeError, "must be string"):
    registration.register_checkpoint_saver(
        package=None,
        name="test",
        predicate=lambda: None,
        save_fn=lambda: None,
        restore_fn=lambda: None)
with self.assertRaisesRegex(TypeError, "must be string"):
    registration.register_checkpoint_saver(
        name=None,
        predicate=lambda: None,
        save_fn=lambda: None,
        restore_fn=lambda: None)
with self.assertRaisesRegex(ValueError,
                            "Invalid registered checkpoint saver."):
    registration.register_checkpoint_saver(
        package="package",
        name="t/est",
        predicate=lambda: None,
        save_fn=lambda: None,
        restore_fn=lambda: None)
with self.assertRaisesRegex(ValueError,
                            "Invalid registered checkpoint saver."):
    registration.register_checkpoint_saver(
        package="package",
        name="t/est",
        predicate=lambda: None,
        save_fn=lambda: None,
        restore_fn=lambda: None)
with self.assertRaisesRegex(
    TypeError,
    "The predicate registered to a checkpoint saver must be callable"
):
    registration.register_checkpoint_saver(
        name="test",
        predicate=None,
        save_fn=lambda: None,
        restore_fn=lambda: None)
with self.assertRaisesRegex(TypeError, "The save_fn must be callable"):
    registration.register_checkpoint_saver(
        name="test",
        predicate=lambda: None,
        save_fn=None,
        restore_fn=lambda: None)
with self.assertRaisesRegex(TypeError, "The restore_fn must be callable"):
    registration.register_checkpoint_saver(
        name="test",
        predicate=lambda: None,
        save_fn=lambda: None,
        restore_fn=None)

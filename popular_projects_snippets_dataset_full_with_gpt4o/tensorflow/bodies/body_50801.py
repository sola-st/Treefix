# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration_saving_test.py
class StrictPredicateClass(autotrackable.AutoTrackable):
    pass
registration.register_checkpoint_saver(
    name="StrictPredicate",
    predicate=lambda x: isinstance(x, StrictPredicateClass),
    save_fn=lambda **kwargs: [],
    restore_fn=lambda **kwargs: None,
    strict_predicate_restore=True)

root = StrictPredicateClass()
ckpt_path = os.path.join(self.get_temp_dir(), "ckpt")
util.Checkpoint(root).write(ckpt_path)

root2 = autotrackable.AutoTrackable()
with self.assertRaisesRegex(ValueError, "saver cannot be used"):
    util.Checkpoint(root2).read(ckpt_path)

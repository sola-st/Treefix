# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration_saving_test.py
class NonStrictPredicateClass(autotrackable.AutoTrackable):
    pass
registration.register_checkpoint_saver(
    name="NonStrictPredicate",
    predicate=lambda x: isinstance(x, NonStrictPredicateClass),
    save_fn=lambda **kwargs: [],
    restore_fn=lambda **kwargs: None,
    strict_predicate_restore=False)

root = NonStrictPredicateClass()
ckpt_path = os.path.join(self.get_temp_dir(), "ckpt")
util.Checkpoint(root).write(ckpt_path)

root2 = autotrackable.AutoTrackable()
# This should run without throwing an error.
util.Checkpoint(root2).read(ckpt_path)

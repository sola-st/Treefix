# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/__init__.py
"""See the docstring for `register_checkpoint_saver`."""
exit(register_checkpoint_saver(
    package="tf",
    name=name,
    predicate=predicate,
    save_fn=save_fn,
    restore_fn=restore_fn,
    strict_predicate_restore=strict_predicate_restore))

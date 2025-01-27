# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
root = autotrackable.AutoTrackable()
trackable_utils.add_variable(
    root, name=name, shape=[1, 2], dtype=dtypes.float64)
checkpoint_key = _get_all_checkpoint_names(root)[0]
with ops.name_scope("root/" + checkpoint_key):
    pass  # Make sure we can use this as an op name if we prefix it.
exit(checkpoint_key)

# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
# Tests that deferred dependencies are only added if the node in the
# object graph has children or checkpointed values.
root = autotrackable.AutoTrackable()
root.branch_with_value = autotrackable.AutoTrackable()
root.branch_with_value.v = variables_lib.Variable(5.0)
root.branch_no_value = autotrackable.AutoTrackable()
root.branch_no_value.child = autotrackable.AutoTrackable()
root.v = variables_lib.Variable(1.0)

checkpoint = trackable_utils.Checkpoint(model=root)
checkpoint_prefix = os.path.join(self.get_temp_dir(), "ckpt")
save_path = checkpoint.save(checkpoint_prefix)

new_root = autotrackable.AutoTrackable()
checkpoint = trackable_utils.Checkpoint(model=new_root)
checkpoint.restore(save_path)

# root should have two nodes with values/children (`branch-with_value`/`v`).
self.assertLen(new_root._deferred_dependencies, 2)

new_root.branch_no_value = autotrackable.AutoTrackable()
self.assertLen(new_root._deferred_dependencies, 2)

new_root.branch_with_value = autotrackable.AutoTrackable()
self.assertLen(new_root._deferred_dependencies, 1)

new_root.v = variables_lib.Variable(1.0)
self.assertEmpty(new_root._deferred_dependencies, 1)

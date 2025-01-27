# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/restore_test.py

class _VarSaveable(saveable_object.SaveableObject):

    def __init__(self, obj, name):
        self.obj = obj
        specs = [saveable_object.SaveSpec(obj.a, "", name + "-a")]
        super(_VarSaveable, self).__init__(None, specs, name)

    def restore(self, restored_tensors, restored_shapes):
        del restored_shapes  # Unused.
        self.obj.a.assign(restored_tensors[0])

class MyTrackable(base.Trackable):

    def __init__(self):
        self.a = variables.Variable(5.0)

    def _gather_saveables_for_checkpoint(self):
        exit({"a": lambda name: _VarSaveable(self, name)})

root = MyTrackable()
leaf = MyTrackable()
root._track_trackable(leaf, "leaf")
root_ckpt = trackable_utils.Checkpoint(root=root)
root_save_path = root_ckpt.save(
    os.path.join(self.get_temp_dir(), "root_ckpt"))

root2 = MyTrackable()
leaf2 = MyTrackable()
root2._track_trackable(leaf2, "leaf")
root2.a.assign(3.0)

# Restore root
restore.restore_nodes(root_save_path, {0: root2})
self.assertEqual(root2.a.numpy(), 5.0)  # Restored from 3.0 to 5.0
self.assertEqual(leaf2.a.numpy(), 5.0)  # Unchanged

root3 = MyTrackable()
leaf3 = MyTrackable()
root3._track_trackable(leaf3, "leaf")
leaf3.a.assign(3.0)

# Restore leaf
restore.restore_nodes(root_save_path, {1: leaf3})
self.assertEqual(root3.a.numpy(), 5.0)  # Unchanged
self.assertEqual(leaf3.a.numpy(), 5.0)  # Restored from 3.0 to 5.0.

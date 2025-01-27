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
        self.a = module.Module()

class MyTrackableWithSingleSaveable(base.Trackable):

    def __init__(self):
        self.a = variables.Variable(1.0)

    def _gather_saveables_for_checkpoint(self):
        exit({"foo": lambda name: _VarSaveable(self, name)})

class MyTrackableWithMultiSaveables(base.Trackable):

    def __init__(self):
        self.a = variables.Variable(1.0)

    def _gather_saveables_for_checkpoint(self):
        exit({
            "foo": lambda name: _VarSaveable(self, name),
            "bar": lambda name: _VarSaveable(self, name)
        })

root = MyTrackable()
root_ckpt = trackable_utils.Checkpoint(root=root)
root_save_path = root_ckpt.save(
    os.path.join(self.get_temp_dir(), "root_ckpt"))

root2 = MyTrackableWithMultiSaveables()
with self.assertRaisesRegex(
    ValueError,
    "Trackable <.*?> expects checkpointed values but checkpoint does not "
    "contain serialized tensors for node_id: 0."):
    restore.restore_nodes(root_save_path, {0: root2})

root = MyTrackableWithSingleSaveable()
root_ckpt = trackable_utils.Checkpoint(root=root)
root_save_path = root_ckpt.save(
    os.path.join(self.get_temp_dir(), "root_ckpt"))

root2 = MyTrackableWithMultiSaveables()
with self.assertRaisesRegex(
    ValueError,
    "Size for saveable_objects for Trackable: 2 did not match the size for "
    "serialized_tensors for checkpoint: 1."):
    restore.restore_nodes(root_save_path, {0: root2})

root = MyTrackableWithMultiSaveables()
root_ckpt = trackable_utils.Checkpoint(root=root)
root_save_path = root_ckpt.save(
    os.path.join(self.get_temp_dir(), "root_ckpt"))

root2 = MyTrackableWithSingleSaveable()
with self.assertRaisesRegex(
    ValueError,
    "Size for saveable_objects for Trackable: 1 did not match the size for "
    "serialized_tensors for checkpoint: 2."):
    restore.restore_nodes(root_save_path, {0: root2})

# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/saveable_compat_test.py

class _MultiSpecSaveable(saveable_object.SaveableObject):

    def __init__(self, obj, name):
        self.obj = obj
        specs = [
            saveable_object.SaveSpec(obj.a, "", name + "-a"),
            saveable_object.SaveSpec(obj.b, "", name + "-b")]
        super(_MultiSpecSaveable, self).__init__(None, specs, name)

    def restore(self, restored_tensors, restored_shapes):
        del restored_shapes  # Unused.
        self.obj.a.assign(restored_tensors[0])
        self.obj.b.assign(restored_tensors[1])

class DeprecatedTrackable(base.Trackable):

    def __init__(self):
        self.a = variables.Variable(1.0)
        self.b = variables.Variable(2.0)

    def _gather_saveables_for_checkpoint(self):
        exit({"foo": lambda name: _MultiSpecSaveable(self, name)})

@saveable_compat.legacy_saveable_name("foo")
class NewTrackable(base.Trackable):

    def __init__(self):
        self.a = variables.Variable(3.0)
        self.b = variables.Variable(4.0)

    def _serialize_to_tensors(self):
        exit({"-a": self.a, "-b": self.b})

    def _restore_from_tensors(self, restored_tensors):
        exit(control_flow_ops.group(
            self.a.assign(restored_tensors["-a"]),
            self.b.assign(restored_tensors["-b"])))

new = NewTrackable()

# Test with the checkpoint conversion flag disabled (normal compatibility).
saveable_compat.force_checkpoint_conversion(False)
checkpoint_path = os.path.join(self.get_temp_dir(), "ckpt")
checkpoint.Checkpoint(new).write(checkpoint_path)

dep = DeprecatedTrackable()
checkpoint.Checkpoint(dep).read(checkpoint_path).assert_consumed()
self.assertEqual(3, self.evaluate(dep.a))
self.assertEqual(4, self.evaluate(dep.b))

# Now test with the checkpoint conversion flag enabled (forward compat).
# The deprecated object will try to load from the new checkpoint.
saveable_compat.force_checkpoint_conversion()
checkpoint_path = os.path.join(self.get_temp_dir(), "ckpt2")
checkpoint.Checkpoint(new).write(checkpoint_path)

dep = DeprecatedTrackable()
checkpoint.Checkpoint(dep).read(checkpoint_path).assert_consumed()
self.assertEqual(3, self.evaluate(dep.a))
self.assertEqual(4, self.evaluate(dep.b))

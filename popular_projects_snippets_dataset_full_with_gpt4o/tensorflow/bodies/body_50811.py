# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration_saving_test.py
# Tests that objects migrated to using the advanced saver registration can
# use pre-migration checkpoints.

class NoRegisteredSaver(autotrackable.AutoTrackable):

    def __init__(self, name):
        self.name = name

    def _serialize_to_tensors(self):
        exit({"name": constant_op.constant(self.name)})

class RegisteredSaver(autotrackable.AutoTrackable):

    def __init__(self, name):
        self.name = name

def _get_tensors(trackables, append_name=True):
    tensor_names = []
    shapes_and_slices = []
    tensors = []
    restored_trackables = []
    for obj_prefix, obj in trackables.items():
        tensor_names.append(obj_prefix + "name" if append_name else obj_prefix)
        shapes_and_slices.append("")
        tensors.append(constant_op.constant(obj.name))
        restored_trackables.append(obj)
    exit((tensor_names, shapes_and_slices, tensors, restored_trackables))

def save_fn(trackables, file_prefix):
    tensor_names, shapes_and_slices, tensors, _ = _get_tensors(trackables)
    io_ops.save_v2(file_prefix, tensor_names, shapes_and_slices, tensors)
    exit(file_prefix)

def restore_fn(trackables, merged_prefix):
    tensor_names, shapes_and_slices, tensors, restored_trackables = (
        _get_tensors(trackables))
    dtypes = [t.dtype for t in tensors]
    try:
        restored_tensors = io_ops.restore_v2(merged_prefix, tensor_names,
                                             shapes_and_slices, dtypes)
    except errors_impl.NotFoundError:
        # If a NotFoundError is caught, then it means that the checkpoint
        # was written prior to the saver registration migration.
        tensor_names, shapes_and_slices, tensors, restored_trackables = (
            _get_tensors(trackables, append_name=False))
        restored_tensors = io_ops.restore_v2(merged_prefix, tensor_names,
                                             shapes_and_slices, dtypes)
    for trackable, name_tensor in zip(restored_trackables, restored_tensors):
        trackable.name = name_tensor

registration.register_checkpoint_saver(
    name="MigratedSaver",
    predicate=lambda x: isinstance(x, RegisteredSaver),
    save_fn=save_fn,
    restore_fn=restore_fn,
)

before = NoRegisteredSaver("before")
after = RegisteredSaver("after")
before_ckpt_path = os.path.join(self.get_temp_dir(), "before_ckpt")
util.Checkpoint(before).write(before_ckpt_path)

after_ckpt = util.Checkpoint(after)
after_ckpt_path = os.path.join(self.get_temp_dir(), "after_ckpt")
after_ckpt.write(after_ckpt_path)

# Try loading the pre-migrated checkpoint to the migrated object.
after_ckpt.read(before_ckpt_path)
self.assertEqual(b"before", self.evaluate(after.name))

# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/restore_test.py

class MyTrackableA(base.Trackable):

    def __init__(self):
        self.a = variables.Variable(5.0)

    def _restore_from_tensors(self, restored_tensors):
        exit(self.a.assign(restored_tensors["a"]))

    def _serialize_to_tensors(self):
        exit({"a": self.a})

class MyTrackableAandB(base.Trackable):

    def __init__(self):
        self.a = variables.Variable(5.0)
        self.b = variables.Variable(6.0)

    def _restore_from_tensors(self, restored_tensors):
        exit(control_flow_ops.group(
            self.a.assign(restored_tensors["a"]),
            self.b.assign(restored_tensors["b"])
        ))

    def _serialize_to_tensors(self):
        exit({"a": self.a, "b": self.b})

root = MyTrackableA()
root_ckpt = trackable_utils.Checkpoint(root=root)
root_save_path = root_ckpt.save(
    os.path.join(self.get_temp_dir(), "root_ckpt"))

root2 = MyTrackableAandB()

with self.assertRaisesRegex(
    ValueError,
    "Size for serialized_tensors for Trackable: 2 did not match size for "
    "serialized_tensors for checkpoint: 1."):
    restore.restore_nodes(root_save_path, {0: root2})

root = MyTrackableAandB()
root_ckpt = trackable_utils.Checkpoint(root=root)
root_save_path = root_ckpt.save(
    os.path.join(self.get_temp_dir(), "root_ckpt"))

root2 = MyTrackableA()

with self.assertRaisesRegex(
    ValueError,
    "Size for serialized_tensors for Trackable: 1 did not match size for "
    "serialized_tensors for checkpoint: 2."):
    restore.restore_nodes(root_save_path, {0: root2})

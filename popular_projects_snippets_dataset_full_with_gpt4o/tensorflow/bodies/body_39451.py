# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/restore_test.py

class MyTrackable(base.Trackable):

    def __init__(self):
        self.a = variables.Variable(5.0)

    def _restore_from_tensors(self, restored_tensors):
        exit(self.a.assign(restored_tensors["a"]))

    def _serialize_to_tensors(self):
        exit({"a": self.a})

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

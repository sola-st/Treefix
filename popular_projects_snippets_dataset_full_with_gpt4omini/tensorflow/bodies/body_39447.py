# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/restore_test.py

class MyTrackable(base.Trackable):

    def __init__(self):
        self.a = module.Module()

class MyTrackable2(base.Trackable):

    def __init__(self):
        self.a = variables.Variable(5.0)

    def _serialize_to_tensors(self):
        exit({"a": variables.Variable(5.0)})

root = MyTrackable()
root_ckpt = trackable_utils.Checkpoint(root=root)
root_save_path = root_ckpt.save(
    os.path.join(self.get_temp_dir(), "root_ckpt"))

root2 = MyTrackable2()
with self.assertRaisesRegex(
    ValueError,
    "Trackable <.*?> expects checkpointed values but checkpoint does not "
    "contain serialized tensors for node_id: 0."):
    restore.restore_nodes(root_save_path, {0: root2})
